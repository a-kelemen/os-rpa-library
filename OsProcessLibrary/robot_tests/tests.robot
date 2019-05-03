*** Settings ***
Library                      OsProcessLibrary

*** Test Cases ***
Create Folder
    [Tags]                   Create Folder
    Create Folder            test_folder_1

Create Folders
    [Tags]                   Create Folder
    Create Folder            test_folder_2/inner_folder

List Folders
    [Tags]                   List Folders
    ${folders_list}=         List Folders
    Should Contain           ${folders_list}  test_folder

List Folders 2
    [Tags]                   List Folders
    ${folders_list}=         List Folders  test_folder_2
    ${list_length}=          Get Length  ${folders_list}
    Should Be Equal          ${list_length}  ${1}

Folder Should Exist
    [Tags]                   Folder Should Exist  Create Folder
    Create Folder            test_folder_3
    Folder Should Exist      test_folder_3

Folder Should Not Exist
    [Tags]                   Folder Should Not Exist
    Folder Should Not Exist  non_existing_folder

Folder Should Not Exist 2
    [Tags]                   Folder Should Not Exist  Create Folder
    Folder Should Not Exist  non_existing_folder
    Create Folder            test_folder_4
    Run Keyword And Expect Error  DirectoryExistException*
        ...  Folder Should Not Exist  test_folder_4

Delete Folder
    [Tags]                   Delete Folder
    Delete Folder            test_folder_1
    Delete Folder            test_folder_2
    Delete Folder            test_folder_3
    Delete Folder            test_folder_4

Delete Folder 2
    [Tags]                   Delete Folder
    Run Keyword And Expect Error  DirectoryNotFoundException*
        ...  Delete Folder   test_folder_1

File Should Exist
    [Tags]                   File Should Exist
    File Should Exist        ..//robot_tests//test_folder//test_file.txt

Create New File
    [Tags]                   Create New File  File Should Exist
    Create New File          test_file_1.txt
    File Should Exist        ..//robot_tests//test_folder//test_file.txt

Create New File 2
    [Tags]                   Create New File  File Should Exist
    Create New File          test_folder/test_file_2.txt
    File Should Exist        test_folder/test_file_2.txt

Create New File 3
    [Tags]                   Create New File  File Should Exist
    Create New File          test_folder//test_file_3.txt
    File Should Exist        //test_folder//test_file_3.txt

List All Files
    [Tags]                   List All Files
    ${file_list}=            List All Files  test_folder
    ${list_size}=            Get Length  ${file_list}
    should be equal          ${list_size}  ${3}

List All Files 2
    [Tags]                   List All Files
    ${file_list}=            List All Files
    Should Contain           ${file_list}  tests.robot

File Should Not Exist
    [Tags]                   File Should Not Exist
    File Should Not Exist    nonexistingfile.xlsx

File Should Not Exist 2
    [Tags]                   File Should Not Exist
    Run Keyword And Expect Error  FileExistException*
        ...  File Should Not Exist  tests.robot

Delete File
    [Tags]                   Delete File  File Should Not Exist
    Delete File              test_file_1.txt
    File Should Not Exist    test_file_1.txt

Delete File 1
    [Tags]                   Delete File  File Should Not Exist
    Delete File              //test_folder//test_file_2.txt
    File Should Not Exist    //test_folder//test_file_2.txt

Delete File 2
    [Tags]                   Delete File  File Should Not Exist
    Delete File              test_folder/test_file_3.txt
    File Should Not Exist    test_folder/test_file_3.txt

Get File Size
    [Tags]                   Get File Size
    ${file_size}=            Get File Size  tests.robot
    Should Be Equal          ${file_size}  ${4}

Get File Size 2
    [Tags]                   Get File Size
    Run Keyword And Expect Error  FileNotFoundException*
        ...  Get File Size  nonexisting.robot

