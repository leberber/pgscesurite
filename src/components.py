
def email_template(
    agence,
    intervention_ou_ronde,
    date_d_intervention,
    heure_d_intervention,
    heure_d_arrive,
    heure_depart,
    nom_d_intervenant,
    rapport_d_intervention,
    motif_du_retard

):
    return f"""
        <!DOCTYPE html>
        <html>

        <head>
        </head>
        <body>
        <div style = "padding-top: 15px; padding: 10px; background-color: gold; margin: 10px; border-radius:10px; text-align:center; font-family: -apple-system,Nunito,BlinkMacSystemFont,Segoe UI,Roboto,sans-seri; font-size:20px; font-weight:bold">PGS Sécurité</div>
        </body style = "font-family: -apple-system,Nunito,BlinkMacSystemFont,Segoe UI,Roboto,sans-seri;">
        <div style=" padding-top: 15px; padding: 10px; background-color: rgb(241, 241, 241); margin: 10px; border-radius: 10px;font-family: -apple-system,Nunito,BlinkMacSystemFont,Segoe UI,Roboto,sans-seri;">
            <div style="display: flex;">
                <div style = "width:170px; font-size:13px"> <strong>Agence</strong>:</div> <div style = "with:160px;font-size:14px"> {agence}</div> 
            </div>
            <div style="display: flex;">
                <div style = "width:170px; font-size:13px"> <strong>Type</strong> :</div>  <div style = "with:160px;font-size:14px"> {intervention_ou_ronde}</div> 
            </div>
            <div style="display: flex;">
                <div style = "width:170px ;font-size:13px"><strong>Date  D'intervention</strong> :</div>  <div style = "with:160px;font-size:14px"> {date_d_intervention}</div> 
            </div>
            <div style="display: flex;">
                <div style = "width:170px ;font-size:13px"><strong>Heure D'intervention</strong> :</div> <div style = "with:160px;font-size:14px"> {heure_d_intervention}</div> 
            </div>
            <div style="display: flex;">
                <div style = "width:170px ;font-size:13px"><strong>Heure D'arrivé</strong> :</div>  <div style = "with:160px;font-size:14px"> {heure_d_arrive}</div> 
            </div>
            <div style="display: flex;">
                <div style = "width:170px;font-size:13px"><strong>Heure du Départ</strong> :</div>  <div style = "with:160px;font-size:14px"> {heure_depart}</div> 
            </div>
            <div style="display: flex;">
                <div style = "width:170px;font-size:13px"><strong>Nom D'intervenant</strong> :</div>  <div style = "with:160px;font-size:14px"> {nom_d_intervenant}</div> 
            </div>
        </div>

        <div style=" padding-top: 15px; padding: 10px; background-color: rgb(241, 241, 241); margin: 10px; border-radius: 10px;font-family: -apple-system,Nunito,BlinkMacSystemFont,Segoe UI,Roboto,sans-seri;">
        <div style = "text-align:center;padding:5px;font-size:14px"><strong>Rapport de L'intervention:</strong></div> 
        <div style = "font-size:14px"> {rapport_d_intervention}</div>
        </div>


        <div style=" padding-top: 15px; padding: 10px; background-color: rgb(241, 241, 241); margin: 10px; border-radius: 10px;font-family: -apple-system,Nunito,BlinkMacSystemFont,Segoe UI,Roboto,sans-seri;">
        <div style = "text-align:center; padding:5px;font-size:14px"><strong>Motif du Retard:</strong></div> 
        <div style = "font-size:14px">{motif_du_retard}</div>
        </div>

        </html>
"""