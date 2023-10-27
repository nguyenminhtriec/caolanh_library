from django.test import TestCase

# =============================================================================
# class YourTestClass(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         print("setUpTestData: Run once to set up non-modified data for all class methods.")
#         pass
# 
#     def setUp(self):
#         print("setUp: Run once for every test method to setup clean data.")
#         pass
# 
#     def test_false_is_false(self):
#         print("Method: test_false_is_false.")
#         self.assertFalse(False)
# 
#     def test_false_is_true(self):
#         print("Method: test_false_is_true.")
#         self.assertTrue(False)
# 
#     def test_one_plus_one_equals_two(self):
#         print("Method: test_one_plus_one_equals_two.")
#         self.assertEqual(1 + 1, 2)
# =============================================================================

from catalog.models import Author

class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Author.objects.create(first_name='Big', last_name='Bob')

    def test_first_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label, 'first name')
        
    def test_last_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('last_name').verbose_name
        self.assertEqual(field_label, 'last name')
        
    def test_date_of_birth_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_birth').verbose_name
        self.assertEqual(field_label, 'date of birth')
        

    def test_date_of_death_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_death').verbose_name
        self.assertEqual(field_label, 'Died')

    def test_first_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('first_name').max_length
        self.assertEqual(max_length, 100)
        
    def test_last_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('last_name').max_length
        self.assertEqual(max_length, 100)

    def test_object_name_is_last_name_comma_first_name(self):
        author = Author.objects.get(id=1)
        expected_object_name = f'{author.last_name}, {author.first_name}'
        self.assertEqual(str(author), expected_object_name)

    def test_get_absolute_url(self):
        author = Author.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(author.get_absolute_url(), '/catalog/author/1')


from catalog.models import Book, Genre, Lang

class BookModelTest(TestCase):

    # @classmethod
    def createBook(self):
        # Set up non-modified objects used by all test methods
        
        Genre.objects.create(name='Fantasy')
        Genre.objects.create(name='Novel')
             
        book = Book.objects.create(
            title ='Lisbon Nights',
            author = Author.objects.create(first_name='Eric', last_name='Remarque'),
            isbn = '4444555566668',
            summary = 'About World War II',
            lang = Lang.objects.create(name='French')                      
        )
        all_genres = Genre.objects.all()
        book.genre.set(all_genres)
        
        return book
        
        
    def test_str(self):
        book = self.createBook()  # Book.objects.get(id=1)
        self.assertEqual(str(book), 'Lisbon Nights')
        
    def test_get_absolute_url(self):
        book = self.createBook()  # Book.objects.get(id=1)
        self.assertEqual(book.get_absolute_url(), '/catalog/book/1')        
        
    def test_book_lang_french(self):
        book = self.createBook()  # Book.objects.get(id=1)
        self.assertEqual(str(book.lang), 'French')
        
    def test_genre_field_is_not_null(self):
        book = self.createBook()  # Book.objects.get(id=1)
        self.assertFalse(book.genre is None)    
        
    def test_book_display_genres(self):
        book = self.createBook()  # Book.objects.get(id=1)
        self.assertEqual(book.display_genre(), 'Fantasy, Novel')    
        