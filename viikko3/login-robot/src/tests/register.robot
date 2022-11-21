*** Settings ***
Resource  resource.robot
Resource  login.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input New Command With Credentials  matti  salasana123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input New Command With Credentials  kalle  salasana123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input New Command With Credentials  jp  salasana123
    Output Should Contain  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Input New Command With Credentials  kalle  passw1
    Output Should Contain  Password must be at least 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command With Credentials  kalle  salasana
    Output Should Contain  Password must contain at least one special character

*** Keywords ***
Input New Command And Create User
    Input New Command With Credentials  kalle  kalle123