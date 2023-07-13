# Student Database Management System
Careful planning is essential to manage educational institutions these days as they have evolved into complex entities with multiple campuses, many departments, different sections, and a large number of students.
The Student Database Management System allows users to set up reminders for the different events and activities that are needed to be organized by the school’s administration department. 
It also enables school authorities to share relevant information with students and teachers.

At the start we have imported My SQL connector module statement so that we can use this module’s methods to communicate with the MySQL database. Then we have defined a function which will let us choose the tables or records we need to check or execute. We have used con to connect each table to the database. After that, we have used Con.cursor () to create a cursor and we have used query to insert the values to the particular table. Cur. Execute is used to send the query to the connection. And fetch all function is used to fetch all records from cursor. We have also used exception handler to ensure that the flow of the program doesn't break when an exception occurs.

# Sample Output

## Main menu:

![image](https://github.com/naundhini27/DBMS_project/assets/75233111/61bd20d6-dae7-4f51-96fe-740de438551f)

## Student Table:

![image](https://github.com/naundhini27/DBMS_project/assets/75233111/13257ff2-100e-491f-bfdc-a51679920060)

## Teachers Table:

![image](https://github.com/naundhini27/DBMS_project/assets/75233111/06bbd2ab-e865-4ddb-9008-6ca10dfd4d71)
