The autotest.py script user the unittest module from python to test that an object has valid values for its attributes. 

The values assigned to the 'Account' object are automatically created by using the Faker module, so that every time it is executed, different
attributes are assigned. The account_validate.py file contains the definition of the Account class, and the definition of the validate_user function 
that checks the validity of the values in each of the Account objects attributes. The scenarion imagined for the use of these two scripts is one in which user accounts
are being migrated from one database to another as objects. To prevent the issue of invalid data being transferred to a new database, all Account objects can be tested by using
the unittest module to created automated tests in a development environment.
