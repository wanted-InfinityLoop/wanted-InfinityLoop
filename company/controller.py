from flask         import jsonify, make_response
from flask_restful import Resource, request

from company.models import *


class CompanyList(Resource):
    def get(self):
        country_code = request.headers.get("x-wanted-language", "ko")
        company_name = request.args.get("query")

        country = Country.query.filter_by(name=country_code).first()

        if country is None:
            return {"message": "COUNTRY_NOT_SUPPORTED"}, 404

        selected_companies = (
            db.session.query(company_countries).filter_by(country_id=country.id).all()
        )

        result = [
            {"company_name": company.translated_name}
            for company in selected_companies
            if company_name in company.translated_name
        ]

        if len(result) == 0 :
            return {"message": "COMPANY NOT FOUND"}, 404

        return result, 200


class GetDetailCompany(Resource):
    def get(self, comp_name):
        header = request.headers.get("x-wanted-language", "ko")
        
        company = Company.query.filter_by(name=comp_name).first()
        country = Country.query.filter_by(name=header).first()

        if not company or not country:
            return make_response(
                jsonify(
                    {"message" : "Company or Language Not Found"}
                ), 404
            )

        company_country = db.session.query(company_countries).filter_by(
            company_id = company.id, 
            country_id = country.id
            ).first().translated_name
        
        company_tag_set  = db.session.query(company_tags).filter_by(company_id=company.id)
        country_tag_list = [db.session.query(country_tags).filter_by(country_id = country.id, tag_id=t.tag_id).first().translated_tag for t in company_tag_set]

        return make_response(
            jsonify(
                {
                    "company_name" : company_country,
                    "tags" : [
                        tag
                    for tag in country_tag_list]
                }
            ), 200
        )
