from flask import Flask, jsonify
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


app = Flask(__name__)

engine = create_engine("sqlite:////Users/timothybryan/Desktop/sqlalchemy-challenge/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station



@app.route('/')
def welcome():
    return "Available routes:"
    
@app.route('/api/v1.0/precipitation')
def precipitation():
    """Return a list of all passenger names, ordered by passenger count
    """
    session = Session(engine)

    # Query all passengers
    results = session.query(Measurement.date, Measurement.prcp).all()

    # Convert list of tuples into normal list
    prcp_data = list(np.ravel(results))

    return jsonify(prcp_data)

@app.route('/api/v1.0/stations')
def stations():
    """Return a list of all passenger names, ordered by passenger count
    """
    session = Session(engine)
    # Query all passengers
    results = session.query(Station.station).all()

    # Convert list of tuples into normal list
    station_data = list(np.ravel(results))

    return jsonify(station_data)
