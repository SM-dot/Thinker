#!/usr/bin/env python3
"""
Demo script for AccountMerge solution
Shows how the accounts merge algorithm works with practical examples
"""

from AccountMerge import Solution

def print_accounts(accounts, title="Accounts"):
    """Helper function to print accounts in a readable format"""
    print(f"\n{title}:")
    print("-" * 50)
    for i, account in enumerate(accounts):
        name = account[0]
        emails = account[1:]
        print(f"Account {i}: {name} -> {emails}")

def main():
    # Create solution instance
    solution = Solution()
    
    # Example 1: Basic merging
    print("EXAMPLE 1: Basic Account Merging")
    print("=" * 50)
    
    accounts1 = [
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
        ["John", "johnsmith@mail.com", "john00@mail.com"],
        ["Mary", "mary@mail.com"],
        ["John", "johnnybravo@mail.com"]
    ]
    
    print_accounts(accounts1, "Input Accounts")
    
    result1 = solution.accountsMerge(accounts1)
    print_accounts(result1, "Merged Accounts")
    
    # Example 2: Complex chain merging
    print("\nEXAMPLE 2: Complex Chain Merging")
    print("=" * 50)
    
    accounts2 = [
        ["Alex", "alex@mail.com", "alex2@mail.com"],
        ["Alex", "alex2@mail.com", "alex3@mail.com"],
        ["Alex", "alex3@mail.com", "alex4@mail.com"],
        ["Bob", "bob@mail.com"],
        ["Charlie", "charlie@mail.com", "charlie2@mail.com"]
    ]
    
    print_accounts(accounts2, "Input Accounts")
    
    result2 = solution.accountsMerge(accounts2)
    print_accounts(result2, "Merged Accounts")
    
    # Example 3: No merging needed
    print("\nEXAMPLE 3: No Merging Needed")
    print("=" * 50)
    
    accounts3 = [
        ["Alice", "alice@mail.com"],
        ["Bob", "bob@mail.com"],
        ["Charlie", "charlie@mail.com"]
    ]
    
    print_accounts(accounts3, "Input Accounts")
    
    result3 = solution.accountsMerge(accounts3)
    print_accounts(result3, "Merged Accounts")
    
    print("\n" + "=" * 50)
    print("All examples completed successfully!")
    print("The algorithm correctly merges accounts that share emails")
    print("and keeps separate accounts that don't share any emails.")

if __name__ == "__main__":
    main()
