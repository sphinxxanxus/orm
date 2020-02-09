from src.masonite.orm.grammer.mysql_grammer import MySQLGrammer 
from src.masonite.orm.blueprint.Blueprint import Blueprint
from src.masonite.orm.grammer.GrammerFactory import GrammerFactory 
import unittest

class TestMySQLUpdateGrammer(unittest.TestCase):


    def setUp(self):
        self.blueprint = Blueprint(GrammerFactory.make('mysql'), table='users')


    def test_can_compile_column(self):
        blueprint = self.blueprint
        to_sql = (
            blueprint.string('name')
        )

        sql = "CREATE TABLE `users` (`name` VARCHAR(255))"
        self.assertEqual(blueprint.to_sql(), sql)

    def test_can_compile_multiple_columns(self):
        blueprint = self.blueprint
        to_sql = (
            blueprint.string('name'),
            blueprint.integer('age'),
        )

        sql = ("CREATE TABLE `users` ("
                "`name` VARCHAR(255), "
                "`age` INT(11)"
            ")"
        )
        self.assertEqual(blueprint.to_sql(), sql)

    def test_can_compile_not_null(self):
        blueprint = self.blueprint
        to_sql = (
            blueprint.string('name', nullable=False),
        )

        sql = ("CREATE TABLE `users` ("
                "`name` VARCHAR(255) NOT NULL"
            ")"
        )
        self.assertEqual(blueprint.to_sql(), sql)

    def test_can_compile_primary_key(self):
        blueprint = self.blueprint
        to_sql = (
            blueprint.increments('id'),
            blueprint.string('name', nullable=False),
        )

        sql = ("CREATE TABLE `users` ("
                "`id` INT AUTO_INCREMENT PRIMARY KEY, "
                "`name` VARCHAR(255) NOT NULL"
            ")"
        )

        self.assertEqual(blueprint.to_sql(), sql)

    def test_can_compile_enum(self):
        blueprint = self.blueprint
        to_sql = (
            blueprint.enum('age', [1,2,3]),
        )

        sql = ("CREATE TABLE `users` ("
                "`age` ENUM('1','2','3')"
            ")"
        )

        self.assertEqual(blueprint.to_sql(), sql)

    def test_can_compile_large_blueprint(self):
        blueprint = self.blueprint
        to_sql = (
            blueprint.string('name', nullable=False),
            blueprint.string('email', nullable=False),
            blueprint.string('password', nullable=False),
            blueprint.integer('age'),
            blueprint.enum('type', ['Open', 'Closed']),
            blueprint.datetime('pick_up'),
            blueprint.binary('profile'),
            blueprint.boolean('of_age'),
            blueprint.char('first_initial', length=4),
            blueprint.date('birthday'),
            blueprint.decimal('credit', 17,6),
            blueprint.text('description'),
            blueprint.unsigned('bank')
        )

        sql = ("CREATE TABLE `users` ("
                "`name` VARCHAR(255) NOT NULL, "
                "`email` VARCHAR(255) NOT NULL, "
                "`password` VARCHAR(255) NOT NULL, "
                "`age` INT(11), "
                "`type` ENUM('Open','Closed'), "
                "`pick_up` DATETIME, "
                "`profile` LONGBLOB, "
                "`of_age` BOOLEAN, "
                "`first_initial` CHAR(4), "
                "`birthday` DATE, "
                "`credit` DECIMAL(17, 6), "
                "`description` TEXT, "
                "`bank` INT UNSIGNED"
            ")"
        )

        self.assertEqual(blueprint.to_sql(), sql)
