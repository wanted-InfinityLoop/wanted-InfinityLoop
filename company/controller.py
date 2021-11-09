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

        return result, 200
