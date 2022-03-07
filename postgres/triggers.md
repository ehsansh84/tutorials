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
```sql
CREATE TRIGGER t BEFORE INSERT OR UPDATE OR DELETE ON your_table
        FOR EACH ROW EXECUTE PROCEDURE change_trigger();
```

#### Refrences:
- [A Short Guide To Debugging PostgreSQL Triggers](https://avilpage.com/2019/04/how-to-debug-postgres-triggers.html)
- [How to log data change in postgresql?](https://stackoverflow.com/questions/13785855/how-to-log-data-change-in-postgresql)
