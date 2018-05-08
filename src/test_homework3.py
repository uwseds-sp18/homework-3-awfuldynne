import unittest
from homework3 import create_dataframe


class HomeworkThreeTest(unittest.TestCase):
    correct_file_path = "../data/class.db"
    invalid_file_path = "../data/not_class.db"

    def test_column_names(self):
        # List of valid column names
        column_list = ['video_id', 'category_id', 'language']
        # Instantiate DataFrame
        df = create_dataframe(HomeworkThreeTest.correct_file_path)
        # Loop through column names to check that each is valid
        result = True
        for column_name in df.columns:
            if column_name not in column_list:
                result = False
        # Assert if any column names are invalid
        self.assertTrue(result)

    def test_number_of_rows(self):
        # Instantiate DataFrame
        df = create_dataframe(HomeworkThreeTest.correct_file_path)
        # Assert if DataFrame has fewer than 10 rows
        self.assertFalse(df.shape[0] < 10)

    def test_columns_are_key(self):
        # Columns that should be a key
        valid_key_columns = ['video_id', 'language']
        # Instantiate DataFrame
        df = create_dataframe(HomeworkThreeTest.correct_file_path)
        grouped_df = df.groupby(valid_key_columns).size()
        # Assert if columns aren't a key
        self.assertFalse(grouped_df[grouped_df > 1].any())

    def test_invalid_path(self):
        # Assert if improper exception is raised
        self.assertRaises(ValueError, create_dataframe, HomeworkThreeTest.invalid_file_path)


if __name__ == '__main__':
    unittest.main()
