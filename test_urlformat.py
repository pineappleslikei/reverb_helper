import unittest
import url_format


class TestUrlFormat(unittest.TestCase):
    def test_url_validate(self):
        url1 = 'https://drive.google.com/file/d/1iC1QiDOi9TI1pF66FyrCVo1rIGRtOwvM/view?usp=sharing'
        url2 = 'https://drive.google.com/drive/u/0/folders/0B-SpeVaSKxvMaW9vdUViRnAyRVk'
        self.assertTrue(url_format.url_validate(url1))
        self.assertIsNone(url_format.url_validate(url2))

    def test_photo_id_strip(self):
        url1 = 'https://drive.google.com/file/d/1iC1QiDOi-9TI1pF66FyrCVo1rIGRtOwvM/view?usp=sharing'
        self.assertEqual(url_format.photo_id_strip(
            url1), '1iC1QiDOi-9TI1pF66FyrCVo1rIGRtOwvM')

    def test_url_format(self):
        self.assertEqual(url_format.url_format('18763-bfGHGCFGfhf87'),
                         'https://drive.google.com/uc?id=18763-bfGHGCFGfhf87&export=download')
        self.assertEqual(url_format.url_format('aaaaaaaa----jhvhgc654GFChgnbvhg'),
                         'https://drive.google.com/uc?id=aaaaaaaa----jhvhgc654GFChgnbvhg&export=download')


if __name__ == '__main__':
    unittest.main()
