*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page


*** Test Cases ***
Register With Valid Username And Password
    Set Username  matti
    Set Password  matti1234
    Set Password Confirmation  matti1234
    Submit Registration Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ML
    Set Password  matti1234
    Set Password Confirmation  matti234
    Submit Registration Credentials
    Register Should Fail With Message  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Username  matti
    Set Password  pw2
    Set Password Confirmation  pw2
    Submit Registration Credentials
    Register Should Fail With Message  Password must be at least 8 characters long

Register With Nonmatching Password And Password Confirmation
    Set Username  matti
    Set Password  password1
    Set Password Confirmation  password2
    Submit Registration Credentials
    Register Should Fail With Message  Passwords don't match

Login After Successful Registration
    Set Username  matti
    Set Password  matti1234
    Set Password Confirmation  matti1234
    Submit Registration Credentials
    Register Should Succeed

    Go To Login Page
    Set Username  matti
    Set Password  matti1234
    Submit Login Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  ml
    Set Password  matti1234
    Set Password Confirmation  matti1234
    Submit Registration Credentials
    Register Should Fail With Message  Username must be at least 3 characters long

    Go To Login Page
    Set Username  ml
    Set Password  matti1234
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password


*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Registration Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Create User And Go To Register Page
    Create User  kalle  kalle123
    Go To Register Page
    Register Page Should Be Open
