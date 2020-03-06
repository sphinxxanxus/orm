import inspect

from ..builder.QueryBuilder import QueryBuilder
from ..grammar.GrammarFactory import GrammarFactory


class BaseTestCaseSelectGrammer:
    def setUp(self):
        self.builder = QueryBuilder(GrammarFactory.make(self.grammar), table="users")

    def test_can_compile_select(self):
        to_sql = self.builder.to_sql()

        sql = getattr(
            self, inspect.currentframe().f_code.co_name.replace("test_", "")
        )()
        self.assertEqual(to_sql, sql)

    def test_can_compile_with_columns(self):
        to_sql = self.builder.select("username", "password").to_sql()
        sql = getattr(
            self, inspect.currentframe().f_code.co_name.replace("test_", "")
        )()
        self.assertEqual(to_sql, sql)

    def test_can_compile_with_where(self):
        to_sql = self.builder.select("username", "password").where("id", 1).to_sql()
        sql = getattr(
            self, inspect.currentframe().f_code.co_name.replace("test_", "")
        )()
        self.assertEqual(to_sql, sql)

    def test_can_compile_or_where(self):
        to_sql = self.builder.where("name", 2).or_where("name", 3).to_sql()
        sql = getattr(
            self, inspect.currentframe().f_code.co_name.replace("test_", "")
        )()
        self.assertEqual(to_sql, sql)

    def test_can_grouped_where(self):
        to_sql = self.builder.where(
            lambda query: query.where("age", 2).where("name", "Joe")
        ).to_sql()
        sql = getattr(
            self, inspect.currentframe().f_code.co_name.replace("test_", "")
        )()
        self.assertEqual(to_sql, sql)

    def test_can_compile_with_several_where(self):
        to_sql = (
            self.builder.select("username", "password")
            .where("id", 1)
            .where("username", "joe")
            .to_sql()
        )
        sql = getattr(
            self, inspect.currentframe().f_code.co_name.replace("test_", "")
        )()
        self.assertEqual(to_sql, sql)

    def test_can_compile_with_several_where_and_limit(self):
        to_sql = (
            self.builder.select("username", "password")
            .where("id", 1)
            .where("username", "joe")
            .limit(10)
            .to_sql()
        )
        sql = getattr(
            self, inspect.currentframe().f_code.co_name.replace("test_", "")
        )()
        self.assertEqual(to_sql, sql)

    def test_can_compile_with_sum(self):
        to_sql = self.builder.sum("age").to_sql()
        sql = getattr(
            self, inspect.currentframe().f_code.co_name.replace("test_", "")
        )()
        self.assertEqual(to_sql, sql)

    def test_can_compile_with_max(self):
        to_sql = self.builder.max("age").to_sql()
        sql = getattr(
            self, inspect.currentframe().f_code.co_name.replace("test_", "")
        )()
        self.assertEqual(to_sql, sql)

    def test_can_compile_with_max_and_columns(self):
        to_sql = self.builder.select("username").max("age").to_sql()
        sql = getattr(
            self, inspect.currentframe().f_code.co_name.replace("test_", "")
        )()
        self.assertEqual(to_sql, sql)

    def test_can_compile_with_max_and_columns_different_order(self):
        to_sql = self.builder.max("age").select("username").to_sql()
        sql = getattr(
            self, inspect.currentframe().f_code.co_name.replace("test_", "")
        )()
        self.assertEqual(to_sql, sql)

    def test_can_compile_with_order_by(self):
        to_sql = self.builder.select("username").order_by("age", "desc").to_sql()
        sql = getattr(
            self, inspect.currentframe().f_code.co_name.replace("test_", "")
        )()
        self.assertEqual(to_sql, sql)

    def test_can_compile_with_group_by(self):
        to_sql = self.builder.select("username").group_by("age").to_sql()
        sql = getattr(
            self, inspect.currentframe().f_code.co_name.replace("test_", "")
        )()
        self.assertEqual(to_sql, sql)

    def test_can_compile_where_in(self):
        to_sql = self.builder.select("username").where_in("age", [1, 2, 3]).to_sql()
        sql = getattr(
            self, inspect.currentframe().f_code.co_name.replace("test_", "")
        )()
        self.assertEqual(to_sql, sql)

    def test_can_compile_where_null(self):
        to_sql = self.builder.select("username").where_null("age").to_sql()
        sql = getattr(
            self, inspect.currentframe().f_code.co_name.replace("test_", "")
        )()
        self.assertEqual(to_sql, sql)

    def test_can_compile_where_not_null(self):
        to_sql = self.builder.select("username").where_not_null("age").to_sql()
        sql = getattr(
            self, inspect.currentframe().f_code.co_name.replace("test_", "")
        )()
        self.assertEqual(to_sql, sql)

    def test_can_compile_count(self):
        to_sql = self.builder.count().to_sql()
        sql = getattr(
            self, inspect.currentframe().f_code.co_name.replace("test_", "")
        )()
        self.assertEqual(to_sql, sql)

    def test_can_compile_count_column(self):
        to_sql = self.builder.count("money").to_sql()
        sql = getattr(
            self, inspect.currentframe().f_code.co_name.replace("test_", "")
        )()
        self.assertEqual(to_sql, sql)

    def test_can_compile_where_column(self):
        to_sql = self.builder.where_column("name", "email").to_sql()
        sql = getattr(
            self, inspect.currentframe().f_code.co_name.replace("test_", "")
        )()
        self.assertEqual(to_sql, sql)

    def test_can_compile_sub_select(self):
        to_sql = self.builder.where_in(
            "name", self.builder.new().select("age")
        ).to_sql()
        sql = getattr(
            self, inspect.currentframe().f_code.co_name.replace("test_", "")
        )()
        self.assertEqual(to_sql, sql)

    def test_can_compile_complex_sub_select(self):
        to_sql = self.builder.where_in(
            "name",
            (
                self.builder.new()
                .select("age")
                .where_in("email", self.builder.new().select("email"))
            ),
        ).to_sql()
        sql = getattr(
            self, inspect.currentframe().f_code.co_name.replace("test_", "")
        )()
        self.assertEqual(to_sql, sql)

    def test_can_compile_sub_select_value(self):
        to_sql = self.builder.where("name", self.builder.new().sum("age")).to_sql()
        sql = getattr(
            self, inspect.currentframe().f_code.co_name.replace("test_", "")
        )()
        self.assertEqual(to_sql, sql)

    def test_can_compile_exists(self):
        to_sql = (
            self.builder.select("age")
            .where_exists(self.builder.new().select("username").where("age", 12))
            .to_sql()
        )
        sql = getattr(
            self, inspect.currentframe().f_code.co_name.replace("test_", "")
        )()
        self.assertEqual(to_sql, sql)

    def test_can_compile_having(self):
        to_sql = self.builder.sum("age").group_by("age").having("age").to_sql()
        sql = getattr(
            self, inspect.currentframe().f_code.co_name.replace("test_", "")
        )()
        self.assertEqual(to_sql, sql)

    def test_can_compile_having_with_expression(self):
        to_sql = self.builder.sum("age").group_by("age").having("age", 10).to_sql()
        sql = getattr(
            self, inspect.currentframe().f_code.co_name.replace("test_", "")
        )()
        self.assertEqual(to_sql, sql)

    def test_can_compile_having_with_greater_than_expression(self):
        to_sql = self.builder.sum("age").group_by("age").having("age", ">", 10).to_sql()
        sql = getattr(
            self, inspect.currentframe().f_code.co_name.replace("test_", "")
        )()
        self.assertEqual(to_sql, sql)

    def test_can_compile_join(self):
        to_sql = self.builder.join(
            "contacts", "users.id", "=", "contacts.user_id"
        ).to_sql()
        sql = getattr(
            self, inspect.currentframe().f_code.co_name.replace("test_", "")
        )()
        self.assertEqual(to_sql, sql)

    def test_can_compile_left_join(self):
        to_sql = self.builder.left_join(
            "contacts", "users.id", "=", "contacts.user_id"
        ).to_sql()
        sql = getattr(
            self, inspect.currentframe().f_code.co_name.replace("test_", "")
        )()
        self.assertEqual(to_sql, sql)

    def test_can_compile_multiple_join(self):
        to_sql = (
            self.builder.join("contacts", "users.id", "=", "contacts.user_id")
            .join("posts", "comments.post_id", "=", "posts.id")
            .to_sql()
        )
        sql = getattr(
            self, inspect.currentframe().f_code.co_name.replace("test_", "")
        )()
        self.assertEqual(to_sql, sql)

    def test_can_compile_limit_and_offset(self):
        to_sql = self.builder.limit(10).offset(10).to_sql()
        sql = getattr(
            self, inspect.currentframe().f_code.co_name.replace("test_", "")
        )()
        self.assertEqual(to_sql, sql)

    def test_can_compile_between(self):
        to_sql = self.builder.between("age", 18, 21).to_sql()
        sql = getattr(
            self, inspect.currentframe().f_code.co_name.replace("test_", "")
        )()
        self.assertEqual(to_sql, sql)
