#!/usr/bin/env python3
"""
Test script for MsafiriiMoney application setup
"""

import os
import sys
from datetime import datetime

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Test if all modules can be imported"""
    print("Testing imports...")
    
    try:
        from app import create_app, db
        print("✓ app.py imported successfully")
    except Exception as e:
        print(f"✗ Error importing app.py: {e}")
        return False
    
    try:
        from models import User, Account, Transfer, Transaction, BankAccount
        print("✓ models.py imported successfully")
    except Exception as e:
        print(f"✗ Error importing models.py: {e}")
        return False
    
    try:
        from forms import LoginForm, RegistrationForm, TransferForm, AccountForm
        print("✓ forms.py imported successfully")
    except Exception as e:
        print(f"✗ Error importing forms.py: {e}")
        return False
    
    try:
        from routes import main_bp, auth_bp
        print("✓ routes.py imported successfully")
    except Exception as e:
        print(f"✗ Error importing routes.py: {e}")
        return False
    
    return True

def test_app_creation():
    """Test if the Flask app can be created"""
    print("\nTesting app creation...")
    
    try:
        from app import create_app
        app = create_app()
        print("✓ Flask app created successfully")
        return True
    except Exception as e:
        print(f"✗ Error creating Flask app: {e}")
        return False

def test_database_models():
    """Test if database models can be instantiated"""
    print("\nTesting database models...")
    
    try:
        from models import User, Account, Transfer, Transaction, BankAccount
        
        # Test User model
        user = User(
            username="testuser",
            email="test@example.com",
            first_name="Test",
            last_name="User"
        )
        user.set_password("password123")
        print("✓ User model works")
        
        # Test Account model
        account = Account(
            account_number="ACC000001",
            account_type="savings",
            balance=1000.00,
            currency="KES"
        )
        print("✓ Account model works")
        
        # Test Transfer model
        transfer = Transfer(
            transfer_id="TXN202412101200001",
            amount=100.00,
            currency="KES",
            description="Test transfer"
        )
        print("✓ Transfer model works")
        
        # Test Transaction model
        transaction = Transaction(
            transaction_id="TXN202412101200002",
            amount=100.00,
            currency="KES",
            transaction_type="transfer_in",
            balance_before=0.00,
            balance_after=100.00,
            description="Test transaction"
        )
        print("✓ Transaction model works")
        
        return True
    except Exception as e:
        print(f"✗ Error testing models: {e}")
        return False

def main():
    """Main test function"""
    print("=" * 50)
    print("MsafiriiMoney Application Setup Test")
    print("=" * 50)
    
    # Test imports
    if not test_imports():
        print("\n❌ Import tests failed!")
        return False
    
    # Test app creation
    if not test_app_creation():
        print("\n❌ App creation test failed!")
        return False
    
    # Test models
    if not test_database_models():
        print("\n❌ Model tests failed!")
        return False
    
    print("\n" + "=" * 50)
    print("✅ All tests passed! MsafiriiMoney is ready to run.")
    print("=" * 50)
    
    print("\nNext steps:")
    print("1. Install dependencies: pip install -r requirements.txt")
    print("2. Set environment variables (SESSION_SECRET)")
    print("3. Run the application: python3 main.py")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
