from manage import db, app
# from app import db

# Base = declarative_base()
# metadata = Base.metadata

class Samples_Metadata(db.Model):
    __tablename__ = 'sample_metadata'

    sample = db.Column(db.Integer, primary_key=True)
    EVENT = db.Column(db.Text)
    ETHNICITY = db.Column(db.Text)
    GENDER = db.Column(db.Text)
    AGE = db.Column(db.Float)
    WFREQ = db.Column(db.Float)
    BBTYPE = db.Column(db.Text)
    LOCATION = db.Column(db.Text)
    COUNTRY012 = db.Column(db.Text)
    ZIP012 = db.Column(db.Text)
    COUNTRY1319 = db.Column(db.Text)
    ZIP1319 = db.Column(db.Text)
    DOG = db.Column(db.Text)
    CAT = db.Column(db.Text)
    IMPSURFACE013 = db.Column(db.Float)
    NPP013 = db.Column(db.Float)
    MMAXTEMP013 = db.Column(db.Float)
    PFC013 = db.Column(db.Float)
    IMPSURFACE1319 = db.Column(db.Text)
    NPP1319 = db.Column(db.Float)
    MMAXTEMP1319 = db.Column(db.Float)
    PFC1319 = db.Column(db.Float)

    def __repr__(self):
        return '<sample_metadata %r>' % (self.name)    

class Samples(db.Model):
    __tablename__ = 'samples'

    otu_id = db.Column(db.Integer, primary_key=True)
    otu_label = db.Column(db.Text)
    _940 = db.Column('940', db.Integer)
    _941 = db.Column('941', db.Integer)
    _943 = db.Column('943', db.Integer)
    _944 = db.Column('944', db.Integer)
    _945 = db.Column('945', db.Integer)
    _946 = db.Column('946', db.Integer)
    _947 = db.Column('947', db.Integer)
    _948 = db.Column('948', db.Integer)
    _949 = db.Column('949', db.Integer)
    _950 = db.Column('950', db.Integer)
    _952 = db.Column('952', db.Integer)
    _953 = db.Column('953', db.Integer)
    _954 = db.Column('954', db.Integer)
    _955 = db.Column('955', db.Integer)
    _956 = db.Column('956', db.Integer)
    _958 = db.Column('958', db.Integer)
    _959 = db.Column('959', db.Integer)
    _960 = db.Column('960', db.Integer)
    _961 = db.Column('961', db.Integer)
    _962 = db.Column('962', db.Integer)
    _963 = db.Column('963', db.Integer)
    _964 = db.Column('964', db.Integer)
    _966 = db.Column('966', db.Integer)
    _967 = db.Column('967', db.Integer)
    _968 = db.Column('968', db.Integer)
    _969 = db.Column('969', db.Integer)
    _970 = db.Column('970', db.Integer)
    _971 = db.Column('971', db.Integer)
    _972 = db.Column('972', db.Integer)
    _973 = db.Column('973', db.Integer)
    _974 = db.Column('974', db.Integer)
    _975 = db.Column('975', db.Integer)
    _978 = db.Column('978', db.Integer)
    _1233 = db.Column('1233', db.Integer)
    _1234 = db.Column('1234', db.Integer)
    _1235 = db.Column('1235', db.Integer)
    _1236 = db.Column('1236', db.Integer)
    _1237 = db.Column('1237', db.Integer)
    _1238 = db.Column('1238', db.Integer)
    _1242 = db.Column('1242', db.Integer)
    _1243 = db.Column('1243', db.Integer)
    _1246 = db.Column('1246', db.Integer)
    _1253 = db.Column('1253', db.Integer)
    _1254 = db.Column('1254', db.Integer)
    _1258 = db.Column('1258', db.Integer)
    _1259 = db.Column('1259', db.Integer)
    _1260 = db.Column('1260', db.Integer)
    _1264 = db.Column('1264', db.Integer)
    _1265 = db.Column('1265', db.Integer)
    _1273 = db.Column('1273', db.Integer)
    _1275 = db.Column('1275', db.Integer)
    _1276 = db.Column('1276', db.Integer)
    _1277 = db.Column('1277', db.Integer)
    _1278 = db.Column('1278', db.Integer)
    _1279 = db.Column('1279', db.Integer)
    _1280 = db.Column('1280', db.Integer)
    _1281 = db.Column('1281', db.Integer)
    _1282 = db.Column('1282', db.Integer)
    _1283 = db.Column('1283', db.Integer)
    _1284 = db.Column('1284', db.Integer)
    _1285 = db.Column('1285', db.Integer)
    _1286 = db.Column('1286', db.Integer)
    _1287 = db.Column('1287', db.Integer)
    _1288 = db.Column('1288', db.Integer)
    _1289 = db.Column('1289', db.Integer)
    _1290 = db.Column('1290', db.Integer)
    _1291 = db.Column('1291', db.Integer)
    _1292 = db.Column('1292', db.Integer)
    _1293 = db.Column('1293', db.Integer)
    _1294 = db.Column('1294', db.Integer)
    _1295 = db.Column('1295', db.Integer)
    _1296 = db.Column('1296', db.Integer)
    _1297 = db.Column('1297', db.Integer)
    _1298 = db.Column('1298', db.Integer)
    _1308 = db.Column('1308', db.Integer)
    _1309 = db.Column('1309', db.Integer)
    _1310 = db.Column('1310', db.Integer)
    _1374 = db.Column('1374', db.Integer)
    _1415 = db.Column('1415', db.Integer)
    _1439 = db.Column('1439', db.Integer)
    _1441 = db.Column('1441', db.Integer)
    _1443 = db.Column('1443', db.Integer)
    _1486 = db.Column('1486', db.Integer)
    _1487 = db.Column('1487', db.Integer)
    _1489 = db.Column('1489', db.Integer)
    _1490 = db.Column('1490', db.Integer)
    _1491 = db.Column('1491', db.Integer)
    _1494 = db.Column('1494', db.Integer)
    _1495 = db.Column('1495', db.Integer)
    _1497 = db.Column('1497', db.Integer)
    _1499 = db.Column('1499', db.Integer)
    _1500 = db.Column('1500', db.Integer)
    _1501 = db.Column('1501', db.Integer)
    _1502 = db.Column('1502', db.Integer)
    _1503 = db.Column('1503', db.Integer)
    _1504 = db.Column('1504', db.Integer)
    _1505 = db.Column('1505', db.Integer)
    _1506 = db.Column('1506', db.Integer)
    _1507 = db.Column('1507', db.Integer)
    _1508 = db.Column('1508', db.Integer)
    _1510 = db.Column('1510', db.Integer)
    _1511 = db.Column('1511', db.Integer)
    _1512 = db.Column('1512', db.Integer)
    _1513 = db.Column('1513', db.Integer)
    _1514 = db.Column('1514', db.Integer)
    _1515 = db.Column('1515', db.Integer)
    _1516 = db.Column('1516', db.Integer)
    _1517 = db.Column('1517', db.Integer)
    _1518 = db.Column('1518', db.Integer)
    _1519 = db.Column('1519', db.Integer)
    _1521 = db.Column('1521', db.Integer)
    _1524 = db.Column('1524', db.Integer)
    _1526 = db.Column('1526', db.Integer)
    _1527 = db.Column('1527', db.Integer)
    _1530 = db.Column('1530', db.Integer)
    _1531 = db.Column('1531', db.Integer)
    _1532 = db.Column('1532', db.Integer)
    _1533 = db.Column('1533', db.Integer)
    _1534 = db.Column('1534', db.Integer)
    _1535 = db.Column('1535', db.Integer)
    _1536 = db.Column('1536', db.Integer)
    _1537 = db.Column('1537', db.Integer)
    _1539 = db.Column('1539', db.Integer)
    _1540 = db.Column('1540', db.Integer)
    _1541 = db.Column('1541', db.Integer)
    _1542 = db.Column('1542', db.Integer)
    _1543 = db.Column('1543', db.Integer)
    _1544 = db.Column('1544', db.Integer)
    _1545 = db.Column('1545', db.Integer)
    _1546 = db.Column('1546', db.Integer)
    _1547 = db.Column('1547', db.Integer)
    _1548 = db.Column('1548', db.Integer)
    _1549 = db.Column('1549', db.Integer)
    _1550 = db.Column('1550', db.Integer)
    _1551 = db.Column('1551', db.Integer)
    _1552 = db.Column('1552', db.Integer)
    _1553 = db.Column('1553', db.Integer)
    _1554 = db.Column('1554', db.Integer)
    _1555 = db.Column('1555', db.Integer)
    _1556 = db.Column('1556', db.Integer)
    _1557 = db.Column('1557', db.Integer)
    _1558 = db.Column('1558', db.Integer)
    _1561 = db.Column('1561', db.Integer)
    _1562 = db.Column('1562', db.Integer)
    _1563 = db.Column('1563', db.Integer)
    _1564 = db.Column('1564', db.Integer)
    _1572 = db.Column('1572', db.Integer)
    _1573 = db.Column('1573', db.Integer)
    _1574 = db.Column('1574', db.Integer)
    _1576 = db.Column('1576', db.Integer)
    _1577 = db.Column('1577', db.Integer)
    _1581 = db.Column('1581', db.Integer)
    _1601 = db.Column('1601', db.Integer)

    def __repr__(self):
        return '<samples %r>' % (self.name)    
