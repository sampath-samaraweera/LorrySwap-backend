from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("mssql+pyodbc://sampath:SampaTH132@64.176.80.42:1433/sampath?driver=ODBC+Driver+17+for+SQL+Server&TrustServerCertificate=yes")

Session = sessionmaker(bind=engine)