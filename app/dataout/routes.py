from flask import Flask, request, jsonify, g, render_template, make_response
from flask_json import FlaskJSON, JsonError, json_response, as_json
from datetime import datetime
import requests
from app import db
from app.models import *
from app.api import bp
import pandas as pd
import io
import requests
from flask import Response
from io import StringIO

@bp.route('/data/covidtests', methods=['GET'])
def sendcovidtests():
    """
    Time series testing data for the province of ontario which reports postives, negatives, under investigation, resolved, deaths and total tested
    Source: Government of Ontario (https://www.ontario.ca/page/2019-novel-coronavirus)
    ---
    tags:
        - Data
    responses:
        200:
            description: '.csv'
            content:
                text/plain:
                    schema:
                        type: string
    """
    df = pd.read_sql_table('covidtests', db.engine)
    resp = make_response(df.to_csv(index=False))
    resp.headers["Content-Disposition"] = "attachment; filename=test_data_on.csv"
    resp.headers["Content-Type"] = "text/csv"
    return resp

@bp.route('/data/caselevel', methods=['GET'])
def sendcaselevel():
    """
    Compiled daily reported data from public health units on confirmed positive cases of COVID-19 in Ontario.
    Case data is as initially reported.
    ---
    tags:
        - Data
    responses:
        200:
            description: '.csv'
            content:
                text/plain:
                    schema:
                        type: string
    """
    df = pd.read_sql_table('confirmedontario', db.engine)
    resp = make_response(df.to_csv(index=False))
    resp.headers["Content-Disposition"] = "attachment; filename=confirmed_positive_on.csv"
    resp.headers["Content-Type"] = "text/csv"
    return resp

@bp.route('/data/covid', methods=['GET'])
def sendcovid():
    """
    Patient level data of covid cases in canada
    Compiled from publicly available information on confirmed and presumptive postive cases during the ongoing COVID-19 outbreak in Canada. Data are entered with each line representing a unique case, including age, sex, health region location, and history of travel where available
    Source: Government of Canada and News Media
    ---
    tags:
        - Data
    responses:
        200:
            description: '.csv'
            content:
                text/plain:
                    schema:
                        type: string
    """
    df = pd.read_sql_table('covid', db.engine)
    resp = make_response(df.to_csv(index=False))
    resp.headers["Content-Disposition"] = "attachment; filename=test_data_canada.csv"
    resp.headers["Content-Type"] = "text/csv"
    return resp

@bp.route('/data/npi', methods=['GET'])
def sendnpi():
    """
    NPI data
    ---
    tags:
        - Data
    responses:
        200:
            description: '.csv'
            content:
                text/plain:
                    schema:
                        type: string
    """
    df = pd.read_sql_table('npiinterventions', db.engine)
    resp = make_response(df.to_csv(index=False))
    resp.headers["Content-Disposition"] = "attachment; filename=npi_canada.csv"
    resp.headers["Content-Type"] = "text/csv"
    return resp

@bp.route('/data/canadamortality', methods=['GET'])
def sendcanadamortality():
    """
    Canadian mortality data
    ---
    tags:
        - Data
    responses:
        200:
            description: '.csv'
            content:
                text/plain:
                    schema:
                        type: string
    """
    df = pd.read_sql_table('canadamortality', db.engine)
    resp = make_response(df.to_csv(index=False))
    resp.headers["Content-Disposition"] = "attachment; filename=canada_mortality.csv"
    resp.headers["Content-Type"] = "text/csv"
    return resp

@bp.route('/data/canadarecovered', methods=['GET'])
def sendcanadarecovered():
    """
    Canadian recovered data
    ---
    tags:
        - Data
    responses:
        200:
            description: '.csv'
            content:
                text/plain:
                    schema:
                        type: string
    """
    df = pd.read_sql_table('canadarecovered', db.engine)
    resp = make_response(df.to_csv(index=False))
    resp.headers["Content-Disposition"] = "attachment; filename=canada_recovered.csv"
    resp.headers["Content-Type"] = "text/csv"
    return resp

@bp.route('/data/internationaldata', methods=['GET'])
def sendinternationaldata():
    """
    Time series data on covid cases in international jurisdictions
    Source: Johns Hopkins University Center for Systems Science and Engineering (JHU CSSE)
    ---
    tags:
        - Data
    responses:
        200:
            description: '.csv'
            content:
                text/plain:
                    schema:
                        type: string
    """
    df = pd.read_sql_table('internationaldata', db.engine)
    resp = make_response(df.to_csv(index=False))
    resp.headers["Content-Disposition"] = "attachment; filename=test_data_intl.csv"
    resp.headers["Content-Type"] = "text/csv"
    return resp

@bp.route('/data/internationalmortality', methods=['GET'])
def sendinternationalmortality():
    """
    Retrieve International mortality data
    ---
    tags:
        - Data
    responses:
        200:
            description: '.csv'
            content:
                text/plain:
                    schema:
                        type: string
    """
    df = pd.read_sql_table('internationalmortality', db.engine)
    resp = make_response(df.to_csv(index=False))
    resp.headers["Content-Disposition"] = "attachment; filename=international_mortality.csv"
    resp.headers["Content-Type"] = "text/csv"
    return resp

@bp.route('/data/internationalrecovered', methods=['GET'])
def sendinternationalrecovered():
    """
    International recovered data
    ---
    tags:
        - Data
    responses:
        200:
            description: '.csv'
            content:
                text/plain:
                    schema:
                        type: string
    """
    df = pd.read_sql_table('internationalrecovered', db.engine)
    resp = make_response(df.to_csv(index=False))
    resp.headers["Content-Disposition"] = "attachment; filename=international_recovered.csv"
    resp.headers["Content-Type"] = "text/csv"
    return resp


@bp.route('/data/icucapacity', methods=['GET'])
def icucapacity():
    """
    Ontario ICU data
    ---
    tags:
        - Data
    responses:
        200:
            description: '.csv'
            content:
                text/plain:
                    schema:
                        type: string
    """
    df = pd.read_sql_table('icucapacity', db.engine)
    resp = make_response(df.to_csv(index=False))
    resp.headers["Content-Disposition"] = "attachment; filename=icucapacity.csv"
    resp.headers["Content-Type"] = "text/csv"
    return resp

@bp.route('/data/phucapacity', methods=['GET'])
def phucapacity():
    """
    ICU Bed and Acute Bed Capacity of Public Health Units of The Province of Ontario
    ---
    tags:
        - Data
    responses:
        200:
            description: '.csv'
            content:
                text/plain:
                    schema:
                        type: string
    """
    df = pd.read_sql_table('phucapacity', db.engine)
    resp = make_response(df.to_csv(index=False))
    resp.headers["Content-Disposition"] = "attachment; filename=icu_capacity_on.csv"
    resp.headers["Content-Type"] = "text/csv"
    return resp

@bp.route('/data/canadatesting', methods=['GET'])
def canadatesting():
    """
    Canada testing data
    ---
    tags:
        - Data
    responses:
        200:
            description: '.csv'
            content:
                text/plain:
                    schema:
                        type: string
    """
    df = pd.read_sql_table('canadatesting', db.engine)
    resp = make_response(df.to_csv(index=False))
    resp.headers["Content-Disposition"] = "attachment; filename=canada_testing.csv"
    resp.headers["Content-Type"] = "text/csv"
    return resp

@bp.route('/data/internationaltesting', methods=['GET'])
def internationaltesting():
    """
    International testing data
    ---
    tags:
        - Data
    responses:
        200:
            description: '.csv'
            content:
                text/plain:
                    schema:
                        type: string
    """
    df = pd.read_sql_table('internationaltesting', db.engine)
    resp = make_response(df.to_csv(index=False))
    resp.headers["Content-Disposition"] = "attachment; filename=international_testing.csv"
    resp.headers["Content-Type"] = "text/csv"
    return resp


@bp.route('/data/mobility', methods=['GET'])
def sendmobility():
    """
    Google mobility data
    ---
    tags:
        - Data
    responses:
        200:
            description: '.csv'
            content:
                text/plain:
                    schema:
                        type: string
    """
    df = pd.read_sql_table('mobility', db.engine)
    resp = make_response(df.to_csv(index=False))
    resp.headers["Content-Disposition"] = "attachment; filename=mobility.csv"
    resp.headers["Content-Type"] = "text/csv"
    return resp

@bp.route('/data/mobilitytransportation', methods=['GET'])
def sendmobilitytransportation():
    """
    Apple mobility data
    ---
    tags:
        - Data
    responses:
        200:
            description: '.csv'
            content:
                text/plain:
                    schema:
                        type: string
    """
    output = io.BytesIO()

    df = pd.read_sql_table('mobilitytransportation', db.engine)
    df_apple = df.loc[df.source == 'Apple']
    df_google = df.loc[df.source == 'Google']

    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df_apple.to_excel(writer, sheet_name='Apple', index=False)
    df_google.to_excel(writer, sheet_name='Google', index=False)

    writer.save()
    resp = make_response(output.getvalue())
    resp.headers["Content-Disposition"] = "attachment; filename=mobilitytransportation.xlsx"
    resp.headers["Content-Type"] = "text/xlsx"
    return resp

@bp.route('/data/governmentresponse', methods=['GET'])
def sendgovernmentresponse():
    """
    Government Response data
    ---
    tags:
        - Data
    responses:
        200:
            description: '.csv'
            content:
                text/plain:
                    schema:
                        type: string
    """
    df = pd.read_sql_table('governmentresponse', db.engine)
    resp = make_response(df.to_csv(index=False))
    resp.headers["Content-Disposition"] = "attachment; filename=governmentresponse.csv"
    resp.headers["Content-Type"] = "text/csv"
    return resp

@bp.route('/data/npiinterventions_usa', methods=['GET'])
def sendnpiinterventions_usa():
    """
    NPI Interventions USA data
    ---
    tags:
        - Data
    responses:
        200:
            description: '.csv'
            content:
                text/plain:
                    schema:
                        type: string
    """
    df = pd.read_sql_table('npiinterventions_usa', db.engine)
    resp = make_response(df.to_csv(index=False))
    resp.headers["Content-Disposition"] = "attachment; filename=npi_usa.csv"
    resp.headers["Content-Type"] = "text/csv"
    return resp


@bp.route('/data/longtermcare', methods=['GET'])
def sendlongtermcare_ontario():
    """
    Ontario Long-term Care Home data
    ---
    tags:
        - Data
    responses:
        200:
            description: '.csv'
            content:
                text/plain:
                    schema:
                        type: string
    """
    df = pd.read_sql_table('longtermcare', db.engine)
    resp = make_response(df.to_csv(index=False))
    resp.headers["Content-Disposition"] = "attachment; filename=longtermcare.csv"
    resp.headers["Content-Type"] = "text/csv"
    return resp


@bp.route('/data/longtermcare_summary', methods=['GET'])
def sendlongtermcare_summary_ontario():
    """
    Ontario Long-term Care Home summary data
    ---
    tags:
        - Data
    responses:
        200:
            description: '.csv'
            content:
                text/plain:
                    schema:
                        type: string
    """
    df = pd.read_sql_table('longtermcare_summary', db.engine)
    resp = make_response(df.to_csv(index=False))
    resp.headers["Content-Disposition"] = "attachment; filename=longtermcare_summary.csv"
    resp.headers["Content-Type"] = "text/csv"
    return resp

@bp.route('/data/longtermcare_nolongerinoutbreak', methods=['GET'])
def sendlongtermcare_nolongerinoutbreak_ontario():
    """
    Ontario Long-term Care Home summary data
    ---
    tags:
        - Data
    responses:
        200:
            description: '.csv'
            content:
                text/plain:
                    schema:
                        type: string
    """
    df = pd.read_sql_table('longtermcare_nolongerinoutbreak', db.engine)
    resp = make_response(df.to_csv(index=False))
    resp.headers["Content-Disposition"] = "attachment; filename=longtermcare_nolongerinoutbreak.csv"
    resp.headers["Content-Type"] = "text/csv"
    return resp


@bp.route('/data/predictivemodel', methods=['GET'])
def sendpredictivemodel():
    """
    Predictive model from https://pechlilab.shinyapps.io/output/
    ---
    tags:
        - Data
    responses:
        200:
            description: '.csv'
            content:
                text/plain:
                    schema:
                        type: string
    """
    df = pd.read_sql_table('predictivemodel', db.engine)
    resp = make_response(df.to_csv(index=False))
    resp.headers["Content-Disposition"] = "attachment; filename=predictivemodel.csv"
    resp.headers["Content-Type"] = "text/csv"
    return resp


@bp.route('/data/ideamodel', methods=['GET'])
def sendideamodel():
    """
    IDEA model from https://art-bd.shinyapps.io/Ontario_Health_Unit_IDEA_model/
    ---
    tags:
        - Data
    responses:
        200:
            description: '.csv'
            content:
                text/plain:
                    schema:
                        type: string
    """
    df = pd.read_sql_table('ideamodel', db.engine)
    resp = make_response(df.to_csv(index=False))
    resp.headers["Content-Disposition"] = "attachment; filename=ideamodel.csv"
    resp.headers["Content-Type"] = "text/csv"
    return resp
