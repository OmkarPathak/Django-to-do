from django.test import Client, TestCase
from django.urls import reverse

from .models import Task, Username


class TaskFlowTests(TestCase):
    """Testes de regressao da migracao Django 2.0 -> 5.2.

    Garantem que o comportamento original do app continua o mesmo.
    """

    def _login(self):
        """Faz o primeiro acesso, que cria o usuario anonimo via cookie."""
        response = self.client.get(reverse('tasks'))
        self.assertEqual(response.status_code, 302)
        username = self.client.cookies['username'].value
        return Username.objects.get(username=username)

    def test_first_visit_creates_user_cookie(self):
        user = self._login()
        self.assertEqual(len(user.username), 32)
        response = self.client.get(reverse('tasks'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks.html')

    def test_add_task(self):
        user = self._login()
        response = self.client.post(reverse('tasks'), {
            'title': 'Estudar evolucao de software',
            'description': 'Ler sobre manutencao adaptativa',
            'priority': 'adanger',
        })
        self.assertEqual(response.status_code, 200)
        task = Task.objects.get(username=user)
        self.assertEqual(task.title, 'Estudar evolucao de software')
        self.assertContains(response, 'Estudar evolucao de software')

    def test_invalid_form_does_not_crash(self):
        self._login()
        response = self.client.post(reverse('tasks'), {'title': '', 'priority': 'adanger'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Task.objects.count(), 0)

    def test_post_without_cookie_redirects(self):
        response = self.client.post(reverse('tasks'), {'title': 'x', 'priority': 'adanger'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 0)

    def test_complete_toggles_task(self):
        user = self._login()
        task = Task.objects.create(username=user, title='t')
        self.client.get(reverse('completed_task', args=[task.id]))
        task.refresh_from_db()
        self.assertEqual(task.complete, 1)
        self.client.get(reverse('completed_task', args=[task.id]))
        task.refresh_from_db()
        self.assertEqual(task.complete, 0)

    def test_delete_task(self):
        user = self._login()
        task = Task.objects.create(username=user, title='t')
        self.client.post(reverse('delete_task', args=[task.id]))
        self.assertFalse(Task.objects.filter(id=task.id).exists())

    def test_delete_task_rejects_get(self):
        user = self._login()
        task = Task.objects.create(username=user, title='t')
        response = self.client.get(reverse('delete_task', args=[task.id]))
        self.assertEqual(response.status_code, 405)
        self.assertTrue(Task.objects.filter(id=task.id).exists())

    def test_delete_task_requires_csrf_token(self):
        user = self._login()
        task = Task.objects.create(username=user, title='t')
        csrf_client = Client(enforce_csrf_checks=True)
        csrf_client.cookies['username'] = user.username
        response = csrf_client.post(reverse('delete_task', args=[task.id]))
        self.assertEqual(response.status_code, 403)
        self.assertTrue(Task.objects.filter(id=task.id).exists())

    def test_cannot_touch_other_users_task(self):
        other = Username.objects.create(username='outro')
        task = Task.objects.create(username=other, title='alheia')
        self._login()
        self.client.post(reverse('delete_task', args=[task.id]))
        self.assertTrue(Task.objects.filter(id=task.id).exists())

    def test_clear_removes_user_and_tasks(self):
        user = self._login()
        Task.objects.create(username=user, title='t')
        response = self.client.post(reverse('clear_username'))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Username.objects.filter(id=user.id).exists())
        self.assertEqual(Task.objects.count(), 0)

    def test_clear_without_cookie_does_not_crash(self):
        response = self.client.post(reverse('clear_username'))
        self.assertEqual(response.status_code, 302)

    def test_clear_rejects_get(self):
        response = self.client.get(reverse('clear_username'))
        self.assertEqual(response.status_code, 405)
