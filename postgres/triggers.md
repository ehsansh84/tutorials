<!-- Space: RD -->
<!-- Title: How to work with Postgres Triggers -->
# How to work with Postgres Triggers

### A simple trigger to log all database changes in a table:
table to store logs:
```sql
CREATE SCHEMA logging;
CREATE TABLE logging.t_history (
        id             serial,
        tstamp         timestamp DEFAULT now(),
        schemaname     text,
        tabname        text,
        operation      text,
        who            text DEFAULT current_user,
        new_val        json,
        old_val        json
);
```
trigger to log changes:
```sql

14
9

This question may seem to be a possible duplicate of some other questions that are related to this topic. I've found some similar questions(some questions were asked years back and discussion on the topic seemed to be almost over). But no feasible solutions were found for my problem. I've a database with plenty of tables with huge amount of data in it. I need to log each and every changes that is happening to the datas that are stored in the tables of the particular database.

For example, I have a table for storing employee details.

id    employeename
 1    ab

And, this data is changed to

id    employeename
 1    cd

So i need to log this data.

ie, employeename

    ab

is changed to

    cd

in the table employee details

I need to log the data every time a change is made to the contents stored in the tables. Is it really possible? If so, how can I do that? What are the steps involved in it? I'm pretty concerned about the size of the log files in such a case. In such a situation what can be a good alternative? I'm using postgresql8.4. Any good suggestion will help me a lot. Thanks in advance.
postgresql
postgresql-8.4
audit-trail
Share
Improve this question
Follow
edited Apr 17, 2018 at 7:33
a_horse_with_no_name
483k8787 gold badges748748 silver badges816816 bronze badges
asked Dec 9, 2012 at 8:30
harry
1,24033 gold badges1111 silver badges3131 bronze badges

    1
    You might want to learn about triggers: postgresql.org/docs/8.4/interactive/triggers.html – 
    mu is too short
    Dec 9, 2012 at 8:51

Add a comment
2 Answers
Sorted by:
14

Very generic trigger function, found there: https://www.cybertec-postgresql.com/en/tracking-changes-in-postgresql/

Table to store the history:

CREATE SCHEMA logging;
CREATE TABLE logging.t_history (
        id             serial,
        tstamp         timestamp DEFAULT now(),
        schemaname     text,
        tabname        text,
        operation      text,
        who            text DEFAULT current_user,
        new_val        json,
        old_val        json
);

The trigger:

CREATE FUNCTION change_trigger() RETURNS trigger AS $$
       BEGIN
         IF TG_OP = 'INSERT'
         THEN INSERT INTO logging.t_history (
                tabname, schemaname, operation, new_val
              ) VALUES (
                TG_RELNAME, TG_TABLE_SCHEMA, TG_OP, row_to_json(NEW)
              );
           RETURN NEW;
         ELSIF  TG_OP = 'UPDATE'
         THEN
           INSERT INTO logging.t_history (
             tabname, schemaname, operation, new_val, old_val
           )
           VALUES (TG_RELNAME, TG_TABLE_SCHEMA, TG_OP, row_to_json(NEW), row_to_json(OLD));
           RETURN NEW;
         ELSIF TG_OP = 'DELETE'
         THEN
           INSERT INTO logging.t_history
             (tabname, schemaname, operation, old_val)
             VALUES (
               TG_RELNAME, TG_TABLE_SCHEMA, TG_OP, row_to_json(OLD)
             );
             RETURN OLD;
         END IF;
       END;
$$ LANGUAGE 'plpgsql' SECURITY DEFINER;
```
Apply trigger to table:
```
CREATE TRIGGER t BEFORE INSERT OR UPDATE OR DELETE ON your_table
        FOR EACH ROW EXECUTE PROCEDURE change_trigger();
```

#### Refrences:
- [A Short Guide To Debugging PostgreSQL Triggers](https://avilpage.com/2019/04/how-to-debug-postgres-triggers.html)
- [How to log data change in postgresql?](https://stackoverflow.com/questions/13785855/how-to-log-data-change-in-postgresql)
