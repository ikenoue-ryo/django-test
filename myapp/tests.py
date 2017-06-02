from django.test import TestCase
from django.urls import reverse

from .models import Post


class PostIndexTests(TestCase):
    """PostIndexビューのテストクラス."""

    def test_get(self):
        """getで通常のアクセスを行う."""
        response = self.client.get(reverse('myapp:post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['post_list'], [])

    def test_1post_and_get(self):
        """データを1件追加し、getアクセスの結果を確認する."""
        post = Post.objects.create(title='こんにちは', text='いいてんきでした')
        response = self.client.get(reverse('myapp:post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context['post_list'], ['<Post: こんにちは>']
        )
        self.assertContains(response, post.title)

    def test_2post_and_get(self):
        """データを2件追加し、getアクセスの結果を確認する."""
        post = Post.objects.create(title='こんにちは', text='いいてんきでした')
        post2 = Post.objects.create(title='こんばんは', text='よるです')
        response = self.client.get(reverse('myapp:post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context['post_list'],
            ['<Post: こんにちは>', '<Post: こんばんは>'],
            ordered=False
        )
        self.assertContains(response, post.title)
        self.assertContains(response, post2.title)


class PostDetailTests(TestCase):
    """PostDetailビューのテストクラス."""

    def test_not_fount_pk_get(self):
        """データを作らないまま、存在しないpkでgetアクセス."""
        response = self.client.get(
            reverse('myapp:post_detail', kwargs={'pk': 1}),
        )
        self.assertEqual(response.status_code, 404)

    def test_get(self):
        """getで通常のアクセスを行う."""
        post = Post.objects.create(title='あいうえお', text='あ')
        response = self.client.get(
            reverse('myapp:post_detail', kwargs={'pk': post.pk}),
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, post.title)
        self.assertContains(response, post.text)


class PostCreateTests(TestCase):
    """PostCreateビューのテストクラス."""

    def test_get(self):
        """getで通常のアクセスを行う."""
        response = self.client.get(reverse('myapp:post_create'))
        self.assertEqual(response.status_code, 200)

    def test_post_null(self):
        """空のデータでpostを行う."""
        data = {}
        response = self.client.post(reverse('myapp:post_create'), data=data)
        self.assertEqual(response.status_code, 200)
        # このフィールドは必須です、のcss名がerrorlist
        self.assertContains(response, 'errorlist')

    def test_post_with_data(self):
        """空のデータでpostを行う."""
        data = {
            'title': 'ハロー',
            'text': 'わーるど',
        }
        response = self.client.post(reverse('myapp:post_create'), data=data)
        # 上手くデータが作れれば、リダイレクト処理です
        self.assertEqual(response.status_code, 302)


class PostUpdateTests(TestCase):
    """PostUpdateビューのテストクラス."""

    def test_not_fount_pk_get(self):
        """データを作らないまま、存在しないpkでgetアクセス."""
        response = self.client.get(
            reverse('myapp:post_update', kwargs={'pk': 1}),
        )
        self.assertEqual(response.status_code, 404)

    def test_get(self):
        """getで通常のアクセスを行う."""
        post = Post.objects.create(title='あいうえお', text='あ')
        response = self.client.get(
            reverse('myapp:post_detail', kwargs={'pk': post.pk}),
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, post.title)
        self.assertContains(response, post.text)


class PostDeleteTests(TestCase):
    """PostDeleteビューのテストクラス."""

    def test_not_fount_pk_get(self):
        """データを作らないまま、存在しないpkでgetアクセス."""
        response = self.client.get(
            reverse('myapp:post_update', kwargs={'pk': 1}),
        )
        self.assertEqual(response.status_code, 404)

    def test_get(self):
        """getで通常のアクセスを行う."""
        post = Post.objects.create(title='あいうえお', text='あ')
        response = self.client.get(
            reverse('myapp:post_detail', kwargs={'pk': post.pk}),
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, post.title)
        self.assertContains(response, post.text)
