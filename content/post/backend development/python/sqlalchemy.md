# Queries



## Query

- `session.query(User).filter(User.first_name == "toto")`

## Expression language

- https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_core_expression_language.htm
- Lower level / closer to sql / rarer / more comprehensive
- `select(User).where(User.first_name == “toto”)`