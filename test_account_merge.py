import unittest
from AccountMerge import Solution

class TestAccountMerge(unittest.TestCase):
    
    def setUp(self):
        self.solution = Solution()
    
    def test_basic_merge(self):
        """Test basic account merging with two accounts sharing an email"""
        accounts = [
            ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
            ["John", "johnsmith@mail.com", "john00@mail.com"],
            ["Mary", "mary@mail.com"],
            ["John", "johnnybravo@mail.com"]
        ]
        
        expected = [
            ["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"],
            ["John", "johnnybravo@mail.com"],
            ["Mary", "mary@mail.com"]
        ]
        
        result = self.solution.accountsMerge(accounts)
        # Sort both result and expected for comparison since order doesn't matter
        result.sort(key=lambda x: x[0])
        expected.sort(key=lambda x: x[0])
        self.assertEqual(result, expected)
    
    def test_multiple_shared_emails(self):
        """Test merging when multiple emails are shared between accounts"""
        accounts = [
            ["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"],
            ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"],
            ["Ethan", "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"],
            ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"],
            ["Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"]
        ]
        
        expected = [
            ["Ethan", "Ethan0@m.co", "Ethan4@m.co", "Ethan5@m.co"],
            ["Fern", "Fern0@m.co", "Fern1@m.co", "Fern5@m.co"],
            ["Gabe", "Gabe0@m.co", "Gabe1@m.co", "Gabe3@m.co"],
            ["Hanzo", "Hanzo0@m.co", "Hanzo1@m.co", "Hanzo3@m.co"],
            ["Kevin", "Kevin0@m.co", "Kevin3@m.co", "Kevin5@m.co"]
        ]
        
        result = self.solution.accountsMerge(accounts)
        result.sort(key=lambda x: x[0])
        expected.sort(key=lambda x: x[0])
        self.assertEqual(result, expected)
    
    def test_complex_merge_chain(self):
        """Test complex merging where accounts form a chain of connections"""
        accounts = [
            ["Alex", "Alex5@m.co", "Alex4@m.co", "Alex0@m.co"],
            ["Ethan", "Ethan3@m.co", "Ethan3@m.co", "Ethan0@m.co"],
            ["Kevin", "Kevin4@m.co", "Kevin2@m.co", "Kevin2@m.co"],
            ["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe2@m.co"],
            ["Gabe", "Gabe3@m.co", "Gabe4@m.co", "Gabe2@m.co"]
        ]
        
        expected = [
            ["Alex", "Alex0@m.co", "Alex4@m.co", "Alex5@m.co"],
            ["Ethan", "Ethan0@m.co", "Ethan3@m.co"],
            ["Gabe", "Gabe0@m.co", "Gabe2@m.co", "Gabe3@m.co", "Gabe4@m.co"],
            ["Kevin", "Kevin2@m.co", "Kevin4@m.co"]
        ]
        
        result = self.solution.accountsMerge(accounts)
        result.sort(key=lambda x: x[0])
        expected.sort(key=lambda x: x[0])
        self.assertEqual(result, expected)
    
    def test_single_account(self):
        """Test with a single account"""
        accounts = [["John", "john@mail.com"]]
        expected = [["John", "john@mail.com"]]
        
        result = self.solution.accountsMerge(accounts)
        self.assertEqual(result, expected)
    
    def test_no_shared_emails(self):
        """Test when no accounts share emails"""
        accounts = [
            ["John", "john@mail.com"],
            ["Mary", "mary@mail.com"],
            ["Bob", "bob@mail.com"]
        ]
        
        expected = [
            ["Bob", "bob@mail.com"],
            ["John", "john@mail.com"],
            ["Mary", "mary@mail.com"]
        ]
        
        result = self.solution.accountsMerge(accounts)
        result.sort(key=lambda x: x[0])
        expected.sort(key=lambda x: x[0])
        self.assertEqual(result, expected)
    
    def test_all_accounts_merge(self):
        """Test when all accounts should be merged due to shared emails"""
        accounts = [
            ["John", "john@mail.com", "johnny@mail.com"],
            ["John", "johnny@mail.com", "john123@mail.com"],
            ["John", "john123@mail.com", "john.doe@mail.com"]
        ]
        
        expected = [["John", "john.doe@mail.com", "john123@mail.com", "john@mail.com", "johnny@mail.com"]]
        
        result = self.solution.accountsMerge(accounts)
        self.assertEqual(result, expected)
    
    def test_empty_accounts(self):
        """Test with empty accounts list"""
        accounts = []
        expected = []
        
        result = self.solution.accountsMerge(accounts)
        self.assertEqual(result, expected)
    
    def test_accounts_with_single_email(self):
        """Test accounts that only have one email each"""
        accounts = [
            ["John", "john@mail.com"],
            ["Mary", "mary@mail.com"],
            ["Bob", "bob@mail.com"]
        ]
        
        expected = [
            ["Bob", "bob@mail.com"],
            ["John", "john@mail.com"],
            ["Mary", "mary@mail.com"]
        ]
        
        result = self.solution.accountsMerge(accounts)
        result.sort(key=lambda x: x[0])
        expected.sort(key=lambda x: x[0])
        self.assertEqual(result, expected)
    
    def test_duplicate_emails_in_same_account(self):
        """Test accounts with duplicate emails within the same account"""
        accounts = [
            ["John", "john@mail.com", "john@mail.com", "johnny@mail.com"],
            ["Mary", "mary@mail.com", "mary@mail.com"]
        ]
        
        expected = [
            ["John", "john@mail.com", "johnny@mail.com"],
            ["Mary", "mary@mail.com"]
        ]
        
        result = self.solution.accountsMerge(accounts)
        result.sort(key=lambda x: x[0])
        expected.sort(key=lambda x: x[0])
        self.assertEqual(result, expected)
    
    def test_leetcode_example(self):
        """Test the example from LeetCode problem description"""
        accounts = [
            ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
            ["John", "johnsmith@mail.com", "john00@mail.com"],
            ["Mary", "mary@mail.com"],
            ["John", "johnnybravo@mail.com"]
        ]
        
        expected = [
            ["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"],
            ["John", "johnnybravo@mail.com"],
            ["Mary", "mary@mail.com"]
        ]
        
        result = self.solution.accountsMerge(accounts)
        result.sort(key=lambda x: x[0])
        expected.sort(key=lambda x: x[0])
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
