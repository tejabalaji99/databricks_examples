# Databricks notebook source
# INCLUDE_HEADER_FALSE
# INCLUDE_FOOTER_FALSE

# COMMAND ----------

class DBAcademyHelper():
    def __init__(self, lesson=None, catalog="main"):
        import re, time

        # Define username
        username = spark.sql("SELECT current_user()").first()[0]
        clean_username = re.sub("[^a-zA-Z0-9]", "_", username)

        self.catalog = catalog
        self.schema = f"dbacademy_{clean_username}"
        self.source_db_name = None

        for c in [ self.catalog, "hive_metastore" ]:
            print(f"\nCreating the schema \"{c}.{self.schema}\"")
            spark.sql(f"CREATE SCHEMA IF NOT EXISTS {c}.{self.schema}")

        spark.sql(f"USE CATALOG {self.catalog}")
        spark.sql(f"USE SCHEMA {self.schema}")

        spark.conf.set("da.catalog", self.catalog)
        spark.conf.set("DA.catalog", self.catalog)
        spark.conf.set("da.schema", self.schema)
        spark.conf.set("DA.schema", self.schema)

        
            
    def cleanup(self):
        for c in [ self.catalog, "hive_metastore" ]:
            print(f"Dropping the schema \"{c}.{self.schema}\"")
            spark.sql(f"DROP SCHEMA IF EXISTS {c}.{self.schema} CASCADE")

da = DBAcademyHelper(catalog=catalog)

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE hive_metastore.`${da.schema}`.movies
# MAGIC (
# MAGIC   _c0 STRING,
# MAGIC   title STRING,
# MAGIC   year STRING,
# MAGIC   length STRING,
# MAGIC   budget STRING,
# MAGIC   rating STRING,
# MAGIC   votes STRING,
# MAGIC   r1 STRING,
# MAGIC   r2 STRING,
# MAGIC   r3 STRING,
# MAGIC   r4 STRING,
# MAGIC   r5 STRING,
# MAGIC   r6 STRING,
# MAGIC   r7 STRING,
# MAGIC   r8 STRING,
# MAGIC   r9 STRING,
# MAGIC   r10 STRING,
# MAGIC   mpaa STRING,
# MAGIC   Action STRING,
# MAGIC   Animation STRING,
# MAGIC   Comedy STRING,
# MAGIC   Drama STRING,
# MAGIC   Documentary STRING,
# MAGIC   Romance STRING,
# MAGIC   Short STRING
# MAGIC );
# MAGIC
# MAGIC INSERT INTO hive_metastore.`${da.schema}`.movies VALUES
# MAGIC   ('49321', 'Story of a Three-Day Pass, The', '1968', '87', '100000', '4.7', '104', '34.5', '14.5', '14.5', '4.5', '4.5', '4.5', '4.5', '4.5', '4.5', '4.5', NULL, '0', '0', '0', '1', '0', '0', '0'),
# MAGIC   ('33056', 'Memphis Belle', '1990', '107', 'NA', '6.7', '3882', '4.5', '4.5', '4.5', '4.5', '4.5', '14.5', '24.5', '24.5', '14.5', '4.5', NULL, '1', '0', '0', '1', '0', '0', '0'),
# MAGIC   ('8585', 'Captain Pirate', '1952', '85', 'NA', '5.8', '9', '0', '0', '0', '14.5', '24.5', '44.5', '14.5', '14.5', '0', '0', NULL, '0', '0', '0', '0', '0', '0', '0'),
# MAGIC   ('18355', 'Flying Elephants', '1928', '17', 'NA', '6.1', '46', '4.5', '14.5', '4.5', '4.5', '14.5', '14.5', '24.5', '4.5', '4.5', '4.5', NULL, '0', '0', '1', '0', '0', '0', '1'),
# MAGIC   ('14824', 'Dr. Giggles', '1992', '95', 'NA', '3.8', '757', '24.5', '4.5', '14.5', '14.5', '14.5', '4.5', '4.5', '4.5', '4.5', '14.5', NULL, '0', '0', '1', '0', '0', '0', '0'),
# MAGIC   ('13607', 'Deviants, The', '2004', '80', 'NA', '5.2', '93', '4.5', '4.5', '4.5', '4.5', '14.5', '24.5', '14.5', '4.5', '4.5', '14.5', 'R', '0', '0', '1', '0', '0', '0', '0'),
# MAGIC   ('4492', 'Bas-fonds, Les', '1936', '90', 'NA', '7.5', '183', '0', '4.5', '4.5', '0', '4.5', '4.5', '34.5', '34.5', '14.5', '14.5', NULL, '0', '0', '0', '1', '0', '0', '0'),
# MAGIC   ('21887', 'Han, Hun, Dirch og Dario', '1962', '106', 'NA', '6.2', '23', '4.5', '0', '4.5', '4.5', '0', '24.5', '14.5', '34.5', '4.5', '4.5', NULL, '0', '0', '1', '0', '0', '1', '0'),
# MAGIC   ('43024', 'Retroactive', '1997', '103', 'NA', '6.3', '796', '4.5', '4.5', '4.5', '4.5', '4.5', '14.5', '24.5', '24.5', '4.5', '4.5', 'R', '0', '0', '0', '0', '0', '0', '0'),
# MAGIC   ('26188', 'James Brothers of Missouri, The', '1949', '167', 'NA', '6.9', '5', '0', '0', '0', '0', '44.5', '44.5', '24.5', '0', '0', '0', NULL, '0', '0', '0', '0', '0', '0', '0'),
# MAGIC   ('27277', 'Kamchatka', '2002', '105', 'NA', '7.5', '442', '4.5', '4.5', '4.5', '4.5', '4.5', '14.5', '24.5', '24.5', '14.5', '14.5', NULL, '0', '0', '0', '1', '0', '0', '0'),
# MAGIC   ('20980', 'Grace and the Storm', '2004', '92', 'NA', '7.7', '52', '14.5', '0', '4.5', '4.5', '4.5', '4.5', '4.5', '4.5', '4.5', '44.5', NULL, '0', '0', '0', '1', '0', '0', '0'),
# MAGIC   ('12792', 'Dead London', '1996', '20', 'NA', '4.5', '15', '4.5', '0', '0', '14.5', '4.5', '4.5', '14.5', '24.5', '14.5', '14.5', NULL, '0', '0', '0', '0', '0', '0', '1'),
# MAGIC   ('605', 'A los que aman', '1998', '98', 'NA', '7.3', '93', '4.5', '4.5', '4.5', '4.5', '4.5', '4.5', '14.5', '34.5', '24.5', '4.5', NULL, '0', '0', '0', '1', '0', '1', '0'),
# MAGIC   ('6405', 'Bloodmoon', '1997', '102', 'NA', '4.1', '86', '4.5', '4.5', '4.5', '14.5', '14.5', '4.5', '14.5', '4.5', '4.5', '14.5', 'R', '1', '0', '0', '0', '0', '0', '0'),
# MAGIC   ('41471', 'Prom Fight: The Marc Hall Story', '2002', '60', 'NA', '6.7', '19', '0', '0', '0', '4.5', '0', '24.5', '14.5', '14.5', '14.5', '34.5', NULL, '0', '0', '0', '0', '1', '0', '0'),
# MAGIC   ('11801', 'Crumb', '1994', '119', 'NA', '7.6', '3528', '4.5', '4.5', '4.5', '4.5', '4.5', '4.5', '14.5', '24.5', '24.5', '24.5', NULL, '0', '0', '0', '0', '1', '0', '0'),
# MAGIC   ('15065', 'Drop Dead Roses', '2001', '93', 'NA', '2', '118', '14.5', '4.5', '4.5', '4.5', '4.5', '4.5', '4.5', '4.5', '4.5', '45.5', 'R', '0', '0', '0', '0', '0', '0', '0'),
# MAGIC   ('10833', 'Commissario Lo Gatto, Il', '1987', '91', 'NA', '5.8', '40', '4.5', '0', '4.5', '4.5', '14.5', '14.5', '14.5', '14.5', '4.5', '24.5', NULL, '0', '0', '1', '0', '0', '0', '0'),
# MAGIC   ('14473', "Don't Drink the Water", '1969', '100', 'NA', '5.5', '147', '4.5', '4.5', '4.5', '4.5', '24.5', '24.5', '14.5', '4.5', '4.5', '4.5', NULL, '0', '0', '1', '0', '0', '0', '0'),
# MAGIC   ('19259', 'Full', '2001', '16', 'NA', '8', '5', '0', '0', '0', '0', '0', '24.5', '24.5', '24.5', '24.5', '24.5', NULL, '0', '0', '0', '1', '0', '0', '1'),
# MAGIC   ('34939', 'Multiple Sidosis', '1970', '10', 'NA', '8.9', '6', '0', '14.5', '0', '0', '0', '14.5', '0', '0', '14.5', '45.5', NULL, '0', '0', '0', '0', '0', '0', '1'),
# MAGIC   ('37772', 'On the Fiddle', '1961', '89', 'NA', '5.5', '41', '4.5', '4.5', '4.5', '14.5', '14.5', '14.5', '4.5', '14.5', '4.5', '24.5', NULL, '0', '0', '1', '0', '0', '0', '0'),
# MAGIC   ('39075', 'Paris by Night', '1988', '103', 'NA', '6.3', '24', '4.5', '4.5', '0', '0', '24.5', '14.5', '24.5', '14.5', '14.5', '4.5', NULL, '0', '0', '0', '1', '0', '0', '0'),
# MAGIC   ('47733', 'So This Is Love', '1953', '101', 'NA', '4.8', '19', '0', '4.5', '4.5', '14.5', '14.5', '14.5', '14.5', '4.5', '4.5', '24.5', NULL, '0', '0', '0', '0', '0', '0', '0'),
# MAGIC   ('1539', 'Alcune signore per bene', '1990', '91', 'NA', '2.8', '6', '14.5', '14.5', '0', '14.5', '45.5', '0', '0', '0', '0', '0', NULL, '0', '0', '0', '0', '0', '0', '0'),
# MAGIC   ('13083', 'Decade for Decision', '1957', '15', 'NA', '3.7', '9', '0', '24.5', '14.5', '14.5', '44.5', '14.5', '0', '0', '0', '0', NULL, '0', '0', '0', '0', '1', '0', '1'),
# MAGIC   ('36778', 'Noc u kuci moje majke', '1991', '96', 'NA', '7.3', '7', '0', '0', '14.5', '0', '0', '14.5', '24.5', '24.5', '0', '14.5', NULL, '0', '0', '0', '0', '0', '0', '0'),
# MAGIC   ('4752', 'Beatniks, The', '1960', '78', 'NA', '2', '105', '45.5', '14.5', '14.5', '4.5', '4.5', '4.5', '4.5', '4.5', '0', '4.5', NULL, '0', '0', '0', '0', '0', '0', '0'),
# MAGIC   ('15821', 'Embryo', '1976', '104', 'NA', '4.6', '136', '4.5', '4.5', '14.5', '24.5', '24.5', '14.5', '4.5', '4.5', '4.5', '4.5', NULL, '0', '0', '0', '0', '0', '0', '0'),
# MAGIC   ('6334', 'Blood Screams', '1988', '75', 'NA', '2.3', '8', '34.5', '24.5', '0', '14.5', '0', '0', '14.5', '0', '0', '14.5', NULL, '0', '0', '0', '0', '0', '0', '0'),
# MAGIC   ('42999', 'Restraining Order', '1999', '98', 'NA', '4.1', '93', '14.5', '4.5', '4.5', '14.5', '14.5', '4.5', '14.5', '14.5', '4.5', '4.5', 'R', '1', '0', '0', '0', '0', '0', '0'),
# MAGIC   ('36594', 'Nirvana', '1997', '113', 'NA', '5.4', '1199', '4.5', '4.5', '4.5', '4.5', '4.5', '14.5', '14.5', '14.5', '14.5', '14.5', 'R', '1', '0', '0', '0', '0', '0', '0'),
# MAGIC   ('57935', 'Yazgi', '2001', '120', 'NA', '7.3', '53', '4.5', '0', '4.5', '4.5', '0', '4.5', '24.5', '24.5', '14.5', '14.5', NULL, '0', '0', '0', '1', '0', '0', '0'),
# MAGIC   ('57453', 'Wo ist mein Schatz?', '1916', '35', 'NA', '6.9', '12', '0', '0', '0', '14.5', '14.5', '4.5', '24.5', '14.5', '14.5', '0', NULL, '0', '0', '0', '0', '0', '0', '1'),
# MAGIC   ('24656', "I'm From Hollywood", '1992', '60', 'NA', '7.2', '144', '4.5', '4.5', '4.5', '4.5', '4.5', '4.5', '14.5', '14.5', '14.5', '44.5', NULL, '0', '0', '0', '0', '1', '0', '0'),
# MAGIC   ('25123', 'In nome del papa re', '1977', '105', 'NA', '7', '35', '0', '0', '4.5', '0', '4.5', '4.5', '34.5', '24.5', '4.5', '14.5', NULL, '0', '0', '0', '1', '0', '0', '0'),
# MAGIC   ('35418', 'Mystery Train', '1989', '113', '2800000', '7.2', '2469', '4.5', '4.5', '4.5', '4.5', '4.5', '4.5', '24.5', '24.5', '14.5', '14.5', NULL, '0', '0', '1', '1', '0', '0', '0'),
# MAGIC   ('42822', 'Reluctant Saint, The', '1962', '105', 'NA', '6.5', '25', '0', '0', '0', '4.5', '4.5', '4.5', '4.5', '24.5', '14.5', '44.5', NULL, '0', '0', '1', '1', '0', '0', '0'),
# MAGIC   ('40981', 'Power', '1986', '111', 'NA', '5.5', '414', '4.5', '4.5', '4.5', '14.5', '14.5', '24.5', '14.5', '14.5', '4.5', '4.5', NULL, '0', '0', '0', '1', '0', '0', '0'),
# MAGIC   ('35054', 'Murder on the Orient Express', '1974', '128', 'NA', '7.1', '4038', '4.5', '4.5', '4.5', '4.5', '4.5', '14.5', '24.5', '24.5', '14.5', '14.5', NULL, '0', '0', '0', '1', '0', '0', '0'),
# MAGIC   ('19012', 'Fresh Airedale', '1945', '7', 'NA', '6.6', '17', '4.5', '0', '0', '4.5', '4.5', '24.5', '14.5', '14.5', '0', '24.5', NULL, '0', '1', '1', '0', '0', '0', '1'),
# MAGIC   ('9162', 'Cellar Dweller', '1988', '77', 'NA', '3.2', '118', '14.5', '14.5', '14.5', '14.5', '4.5', '4.5', '4.5', '4.5', '4.5', '14.5', NULL, '0', '0', '0', '0', '0', '0', '0'),
# MAGIC   ('8339', 'Camarote de lujo', '1959', '95', 'NA', '6.4', '6', '0', '0', '0', '0', '0', '45.5', '0', '0', '34.5', '14.5', NULL, '0', '0', '1', '0', '0', '0', '0'),
# MAGIC   ('36317', 'Night Key', '1937', '68', 'NA', '6.5', '14', '0', '0', '0', '0', '4.5', '44.5', '14.5', '14.5', '0', '24.5', NULL, '0', '0', '0', '0', '0', '0', '0'),
# MAGIC   ('44445', 'Sahara Hare', '1955', '7', 'NA', '7.7', '51', '4.5', '4.5', '0', '4.5', '4.5', '4.5', '14.5', '34.5', '4.5', '24.5', NULL, '0', '1', '1', '0', '0', '0', '1'),
# MAGIC   ('53170', 'Treca sreca', '1995', '90', 'NA', '6.2', '15', '14.5', '0', '0', '0', '14.5', '14.5', '4.5', '4.5', '4.5', '44.5', NULL, '0', '0', '1', '0', '0', '0', '0'),
# MAGIC   ('11467', 'Crack in the Floor, A', '2000', '90', 'NA', '2.5', '199', '44.5', '14.5', '14.5', '4.5', '4.5', '4.5', '4.5', '4.5', '4.5', '14.5', 'R', '0', '0', '0', '0', '0', '0', '0'),
# MAGIC   ('9435', 'Charlie Bravo', '1980', '94', 'NA', '5.2', '12', '4.5', '0', '0', '34.5', '14.5', '0', '14.5', '14.5', '0', '4.5', NULL, '0', '0', '0', '0', '0', '0', '0'),
# MAGIC   ('1200', 'Afrita hanem', '1947', '97', 'NA', '4.7', '7', '0', '0', '0', '14.5', '0', '0', '44.5', '24.5', '14.5', '0', NULL, '0', '0', '1', '0', '0', '1', '0');
# MAGIC   
# MAGIC SELECT col1 AS `Object`,col2 AS `Name`
# MAGIC FROM VALUES
# MAGIC   ('Catalog','${da.catalog}'),
# MAGIC   ('Schema','${da.schema}')

# COMMAND ----------

external_delta_table = 'dbfs:///FileStore/tables/test.delta'
spark.conf.set("da.external_delta_table", external_delta_table)

df = spark.range(20)
(df.write
   .format("delta")
   .mode('overwrite')
   .save(external_delta_table))

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS hive_metastore.${da.schema}.test_external;
# MAGIC CREATE TABLE hive_metastore.${da.schema}.test_external
# MAGIC   LOCATION '${da.external_delta_table}'
