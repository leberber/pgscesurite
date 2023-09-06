from dash import Dash, dcc, html, Input, Output, callback, no_update, State
import dash_mantine_components as dmc
from dash_iconify import DashIconify
from datetime import datetime
from zoneinfo import ZoneInfo
from components import email_template
import smtplib

from email.message import EmailMessage





app = Dash(__name__)
server = app.server

paris_now = datetime.now(tz=ZoneInfo("Europe/Paris"))

app.layout =  dmc.LoadingOverlay(
    html.Div(
    children = [
        html.Div(id = 'envoyer_email_alert'),
    
      dmc.Modal(
            id="modal_report_d_intervention", fullScreen=True, zIndex=10000,
            children = [
                dmc.Center( dmc.Image(src="/assets/pgs.png", alt="superman", width=50)),
                html.Div(id= 'email_ouput'),
                html.Div(
                    style={'padding':'10px'},
                    children = [
                         dmc.Button(
                             children = [
                                  "Envoyer",
                             ],
                           
                            id = 'envoyer_l_email',
                            variant="outline",
                            fullWidth=True,
                            color='yellow',
                            # rightIcon=DashIconify(icon="streamline:mail-send-email-send-email-paper-airplane"),
                            # 
                        ),

                    ]
                ),
       
            ]
        ),
    html.Div(
        className = 'form_div',
        children = [
            
            dmc.Center( dmc.Image(src="/assets/pgs.png", alt="superman", width=50)),
            dmc.TextInput(
                id = 'agence',
                label="Agence",
                placeholder="Agence",
                required=True,
                rightSection=DashIconify(icon="map:insurance-agency"),
            ),
            dmc.Space(h=15),
            dmc.SegmentedControl(
                id = 'intervention_ou_ronde',
                orientation="horizontal",
                fullWidth=True,
                data=['Ronde', 'Intervention'],
                value = 'Ronde'
            ),
            dmc.DatePicker(
                id = 'date_d_intervention',
                label="Date",
                value=paris_now.date(),
                inputFormat="DD-MM-YYYY",
                required=True,
                rightSection=DashIconify(icon="clarity:date-line"),
            ),
            dmc.TimeInput(
                id = 'heure_d_intervention',
                
                label="Heure D'intervention",  required=True, rightSection=DashIconify(icon="carbon:time"),
                
            ),
            dmc.TimeInput(
                id = 'heure_d_arrive',
                label="Heure D'arrivé",  required=True, rightSection=DashIconify(icon="carbon:time"),
            ),
            dmc.TimeInput(
                id = 'heure_depart',
                label="Heure de Départ ",  required=True, rightSection=DashIconify(icon="carbon:time"),
                # value=paris_now.strftime("%m/%d/%Y, %H:%M:%S"), datetime.time(15, 5)
            
            ),
            dmc.TextInput(
                id = 'nom_d_intervenant',
                label="Intervenant",
                placeholder="Nom et Prenom",
                required=True, 
                rightSection=DashIconify(icon="material-symbols:person-outline"),
                
            ),
            dmc.Textarea(
                id = 'rapport_d_intervention',
                label="Rapport de L'intervention",
                placeholder="Rapport de L'intervention",
                autosize=True,
                required=True,
                # minRows=2,
            ),
            dmc.Textarea(
                id = 'motif_du_retard',
                label="Motif du Retard",
                placeholder="Motif du Retard",
                autosize=True,
                # required=True,
                # minRows=2,
            ),
            dmc.Space(h=25),
            dmc.Button(
                "Générer",
                id = 'generer_l_email',
                variant="outline",
                fullWidth=True,
                color='yellow',
                rightIcon=DashIconify(icon="codicon:run-all"),
                # streamline:mail-send-email-send-email-paper-airplane
            ),
        ]

    ),
    dcc.Store(id = 'donne_d_intervention'),
   


    ]




    

))



@callback(
    Output("email_ouput", "children"), 
    Output("donne_d_intervention", "data"), 

    State("agence", "value"),
    State("intervention_ou_ronde", "value"),
    State("date_d_intervention", "value"),
    State("heure_d_intervention", "value"),
    State("heure_d_arrive", "value"),
    State("heure_depart", "value"),
    State("nom_d_intervenant", "value"),
    State("rapport_d_intervention", "value"),
    State("motif_du_retard", "value"),
    Input("generer_l_email", "n_clicks"),
    prevent_initial_call=True
    )
def detail_d_intervention(
    agence, 
    intervention_ou_ronde,
    date_d_intervention,
    heure_d_intervention,
    heure_d_arrive,
    heure_depart,
 
    nom_d_intervenant,
    rapport_d_intervention,
    motif_du_retard,
       envoyer_l_email,
    ):

    
    heure_d_intervention =datetime.fromisoformat(heure_d_intervention).time()
    heure_d_arrive =datetime.fromisoformat(heure_d_arrive).time()
    heure_depart =datetime.fromisoformat(heure_depart).time()
    rapport = {
        "Agence":   agence, 
        "Type" :intervention_ou_ronde,
        "Date  D'intervention": date_d_intervention,
        "Heure D'intervention"  : heure_d_intervention,
        "Heure D'arrivé"  : heure_d_arrive,
        "Heure du Départ"  : heure_depart,
        "Nom D'intervenant"  : nom_d_intervenant,
        "Rapport de L'intervention"  : rapport_d_intervention,
        "Motif du Retard"  : motif_du_retard
    }

    output = []
    block_output= []
    blocks = ["Rapport de L'intervention", "Motif du Retard"]
    for key, value in rapport.items():
        if key not in blocks:
            block_output.append(
                dmc.Group(
                    children = [
                        dmc.Text(
                            className = 'rapport_key',
                            children = [
                                key+' :'
                            ]
                        ),
                        dmc.Text(
                            className = 'rapport_value',
                            children = [
                                value
                            ]
                        ),
                        
                    ]
                )

            )
        else:
            output.append(
                html.Div(
                        className = 'text_area_field ',
                    children = [
                        dmc.Center(
                                 dmc.Text(
                            className = 'rapport_key ',
                            children = [
                                key+' :'
                            ]
                        ),
                        ),
                   
                        dmc.Text(
                            className = 'rapport_value',
                            children = [
                                value
                            ]
                        ),
                        
                    ]
                )

            )

        

    
    return html.Div(children = [ html.Div(block_output,  className = 'key_value_group'), html.Div(output),]), rapport
    # return dash_dangerously_set_inner_html.DangerouslySetInnerHTML(email_template()),rapport

@callback(
    Output("envoyer_email_alert", "children"), 
    State("donne_d_intervention", "data"),

    Input("envoyer_l_email", "n_clicks"),
    prevent_initial_call=True
    )
def detail_d_intervention(data, envoyer_l_email):
    print(data)
    msg = EmailMessage()
    EMAIL_ADDRESS = 'pgs.paris.securite@gmail.com'
    EMAIL_PASSWORD = 'xilbixwchqmpbwhs'
    msg['Subject'] = "Rapport D'intervention"
    msg['From'] = EMAIL_ADDRESS

    msg['To'] = 'interventions@altair-securite.fr,exploitation@pgs-securite.fr,guerroucheaziz@gmail.com,dizaybouthkem@gmail.com'
    msg.set_content(
        email_template(
            data["Agence"],
            data["Type"],
            data["Date  D'intervention"],
            data["Heure D'intervention"],
            data["Heure D'arrivé"],
            data["Heure du Départ"],
            data["Nom D'intervenant"],
            data["Rapport de L'intervention"],
            data["Motif du Retard"]), 
        subtype='html'
    )
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
            return  dmc.Alert(
                    "Les emails ont été envoyés avec succès",
                    title="Email envoyé!",
                    id="envoyer_email_alert",
                    color="green",
                    withCloseButton=True,
                )
    except Exception as e: 
        return  dmc.Alert(
                    f"Les e-mails n'ont pas été envoyés pour la raison suivante{repr(e)}",
                    title="l'e-mail n'a pas été envoyé!",
                    id="envoyer_email_alert",
                    color="red",
                    withCloseButton=True,
                )
             



@callback(
    Output("modal_report_d_intervention", "opened"),
    Input("generer_l_email", "n_clicks"),
    Input("envoyer_l_email", "n_clicks"),
    State("modal_report_d_intervention", "opened"),
    prevent_initial_call=True,
)
def toggle_modal(generer_l_email, envoyer_l_email, opened):
    return not opened




if __name__ == "__main__":
    app.run_server(debug=True)