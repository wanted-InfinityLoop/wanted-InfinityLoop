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
            ).first()
        
        if not company_country:
            return make_response(
                jsonify(
                    {"message" : "Company Does Not Exist"}
                ), 404
            )

        company_tag_set  = db.session.query(company_tags).filter_by(company_id=company.id)
        country_tag_list = [db.session.query(country_tags).filter_by(country_id = country.id, tag_id=t.tag_id).first().translated_tag for t in company_tag_set]

        return make_response(
            jsonify(
                {
                    "company_name" : company_country.translated_name,
                    "tags" : [
                        tag
                    for tag in country_tag_list]
                }
            ), 200
        )


class CompanyCreateView(Resource):
    def post(self):
        try:
            tag_list      = []
            params        = request.get_json()
            country_code  = request.headers.get("x-wanted-language")
            company_infor = list(params["company_name"].items())
            
            if not db.session.query(db.session.query(Company).filter_by(name=company_infor[0][1]).exists()).scalar():
                company_entity = Company(name=company_infor[0][1])
                db.session.add(company_entity)
                db.session.commit()
            else:
                company_entity = Company.query.filter_by(name=company_infor[0][1]).first()

            for language, translated_company in company_infor:
                if not db.session.query(db.session.query(Country).filter_by(name=language).exists()).scalar():
                    country = Country(name=language)
                    db.session.add(country)
                    db.session.commit()
                else:
                    country = Country.query.filter_by(name=language).first()

                com_country = company_countries.insert().values(
                    country_id=country.id,
                    company_id=company_entity.id, 
                    translated_name=translated_company 
                )
                db.session.execute(com_country)
                db.session.commit()
            
            for tag in params["tags"]:
                tag_infor  = list(tag['tag_name'].items())
                tag_entity = Tag(name=tag_infor[0][1])
                db.session.add(tag_entity)
                db.session.commit()
                
                for key, value in tag_infor:
                    if key == country_code:
                        tag_list.append(value)

                    country     = Country.query.filter_by(name=key).first()
                    country_tag = country_tags.insert().values(
                        country_id=country.id,
                        tag_id=tag_entity.id,
                        translated_tag=value
                    )
                    db.session.execute(country_tag)
                    db.session.commit()
        
                com_tag = company_tags.insert().values(
                    company_id=company_entity.id, 
                    tag_id= tag_entity.id
                    )
                db.session.execute(com_tag)
                db.session.commit()
            
            company_name = params["company_name"][country_code]
            tags         = tag_list
            return({"company_name": company_name, "tags":tags}, 200)
        
        except:
            return({"message":"duplicate data"}, 409)