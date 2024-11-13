import streamlit as st
import pandas as pd
from io import BytesIO
from xlsxwriter.utility import xl_col_to_name
from datetime import datetime


from nba_api.live.nba.endpoints._base import Endpoint
from nba_api.live.nba.library.http import NBALiveHTTP




def to_excel(df):
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Dados')
    # Precisa definir o cursor de volta ao início para leitura
    output.seek(0)
    return output.read()

class BoxScore(Endpoint):
    endpoint_url = "boxscore/boxscore_{game_id}.json"
    expected_data = {
        "meta": {
            "version": 1,
            "code": 200,
            "request": "http://nba.cloud/games/0022000180/boxscore?Format=json",
            "time": "2021-01-15 23:51:25.282704",
        },
        "game": {
            "gameId": "0022000180",
            "gameTimeLocal": "2021-01-15T19:30:00-05:00",
            "gameTimeUTC": "2021-01-16T00:30:00Z",
            "gameTimeHome": "2021-01-15T19:30:00-05:00",
            "gameTimeAway": "2021-01-15T19:30:00-05:00",
            "gameEt": "2021-01-15T19:30:00-05:00",
            "duration": 125,
            "gameCode": "20210115/ORLBOS",
            "gameStatusText": "Final",
            "gameStatus": 3,
            "regulationPeriods": 4,
            "period": 4,
            "gameClock": "PT00M00.00S",
            "attendance": 0,
            "sellout": "0",
            "arena": {
                "arenaId": 17,
                "arenaName": "TD Garden",
                "arenaCity": "Boston",
                "arenaState": "MA",
                "arenaCountry": "US",
                "arenaTimezone": "America/New_York",
            },
            "officials": [
                {
                    "personId": 201638,
                    "name": "Brent Barnaky",
                    "nameI": "B. Barnaky",
                    "firstName": "Brent",
                    "familyName": "Barnaky",
                    "jerseyNum": "36",
                    "assignment": "OFFICIAL1",
                }
            ],
            "homeTeam": {
                "teamId": 1610612738,
                "teamName": "Celtics",
                "teamCity": "Boston",
                "teamTricode": "BOS",
                "score": 124,
                "inBonus": "1",
                "timeoutsRemaining": 2,
                "periods": [{"period": 1, "periodType": "REGULAR", "score": 34}],
                "players": [
                    {
                        "status": "ACTIVE",
                        "order": 1,
                        "personId": 1627759,
                        "jerseyNum": "7",
                        "position": "SF",
                        "starter": "1",
                        "oncourt": "0",
                        "played": "1",
                        "statistics": {
                            "assists": 8,
                            "blocks": 0,
                            "blocksReceived": 0,
                            "fieldGoalsAttempted": 12,
                            "fieldGoalsMade": 6,
                            "fieldGoalsPercentage": 0.5,
                            "foulsOffensive": 0,
                            "foulsDrawn": 4,
                            "foulsPersonal": 1,
                            "foulsTechnical": 0,
                            "freeThrowsAttempted": 7,
                            "freeThrowsMade": 7,
                            "freeThrowsPercentage": 1.0,
                            "minus": 50.0,
                            "minutes": "PT25M01.00S",
                            "minutesCalculated": "PT25M",
                            "plus": 65.0,
                            "plusMinusPoints": 15.0,
                            "points": 21,
                            "pointsFastBreak": 0,
                            "pointsInThePaint": 6,
                            "pointsSecondChance": 0,
                            "reboundsDefensive": 2,
                            "reboundsOffensive": 0,
                            "reboundsTotal": 2,
                            "steals": 1,
                            "threePointersAttempted": 5,
                            "threePointersMade": 2,
                            "threePointersPercentage": 0.4,
                            "turnovers": 2,
                            "twoPointersAttempted": 7,
                            "twoPointersMade": 4,
                            "twoPointersPercentage": 0.5714285714285711,
                        },
                        "name": "Jaylen Brown",
                        "nameI": "J. Brown",
                        "firstName": "Jaylen",
                        "familyName": "Brown",
                    }
                ],
                "statistics": {
                    "assists": 25,
                    "assistsTurnoverRatio": 2.27272727272727,
                    "benchPoints": 66,
                    "biggestLead": 29,
                    "biggestLeadScore": "72-101",
                    "biggestScoringRun": 13,
                    "biggestScoringRunScore": "72-101",
                    "blocks": 4,
                    "blocksReceived": 1,
                    "fastBreakPointsAttempted": 9,
                    "fastBreakPointsMade": 5,
                    "fastBreakPointsPercentage": 0.555555555555556,
                    "fieldGoalsAttempted": 88,
                    "fieldGoalsEffectiveAdjusted": 0.607954545454545,
                    "fieldGoalsMade": 45,
                    "fieldGoalsPercentage": 0.511363636363636,
                    "foulsOffensive": 0,
                    "foulsDrawn": 16,
                    "foulsPersonal": 18,
                    "foulsTeam": 18,
                    "foulsTechnical": 0,
                    "foulsTeamTechnical": 0,
                    "freeThrowsAttempted": 19,
                    "freeThrowsMade": 17,
                    "freeThrowsPercentage": 0.894736842105263,
                    "leadChanges": 4,
                    "minutes": "PT240M00.00S",
                    "minutesCalculated": "PT240M",
                    "points": 124,
                    "pointsAgainst": 97,
                    "pointsFastBreak": 13,
                    "pointsFromTurnovers": 16,
                    "pointsInThePaint": 48,
                    "pointsInThePaintAttempted": 36,
                    "pointsInThePaintMade": 24,
                    "pointsInThePaintPercentage": 0.666666666666666,
                    "pointsSecondChance": 11,
                    "reboundsDefensive": 39,
                    "reboundsOffensive": 6,
                    "reboundsPersonal": 45,
                    "reboundsTeam": 6,
                    "reboundsTeamDefensive": 2,
                    "reboundsTeamOffensive": 4,
                    "reboundsTotal": 51,
                    "secondChancePointsAttempted": 6,
                    "secondChancePointsMade": 4,
                    "secondChancePointsPercentage": 0.666666666666666,
                    "steals": 7,
                    "threePointersAttempted": 42,
                    "threePointersMade": 17,
                    "threePointersPercentage": 0.40476190476190504,
                    "timeLeading": "PT47M16.00S",
                    "timesTied": 0,
                    "trueShootingAttempts": 96.36,
                    "trueShootingPercentage": 0.6434205064342051,
                    "turnovers": 10,
                    "turnoversTeam": 1,
                    "turnoversTotal": 11,
                    "twoPointersAttempted": 46,
                    "twoPointersMade": 28,
                    "twoPointersPercentage": 0.608695652173913,
                },
            },
            "awayTeam": {
                "teamId": 1610612753,
                "teamName": "Magic",
                "teamCity": "Orlando",
                "teamTricode": "ORL",
                "score": 97,
                "inBonus": "1",
                "timeoutsRemaining": 2,
                "periods": [{"period": 1, "periodType": "REGULAR", "score": 28}],
                "players": [
                    {
                        "status": "ACTIVE",
                        "order": 1,
                        "personId": 203516,
                        "jerseyNum": "11",
                        "position": "SF",
                        "starter": "1",
                        "oncourt": "0",
                        "played": "1",
                        "statistics": {
                            "assists": 0,
                            "blocks": 0,
                            "blocksReceived": 0,
                            "fieldGoalsAttempted": 4,
                            "fieldGoalsMade": 1,
                            "fieldGoalsPercentage": 0.25,
                            "foulsOffensive": 0,
                            "foulsDrawn": 0,
                            "foulsPersonal": 3,
                            "foulsTechnical": 0,
                            "freeThrowsAttempted": 0,
                            "freeThrowsMade": 0,
                            "freeThrowsPercentage": 0.0,
                            "minus": 41.0,
                            "minutes": "PT14M34.00S",
                            "minutesCalculated": "PT14M",
                            "plus": 36.0,
                            "plusMinusPoints": -5.0,
                            "points": 2,
                            "pointsFastBreak": 0,
                            "pointsInThePaint": 2,
                            "pointsSecondChance": 0,
                            "reboundsDefensive": 1,
                            "reboundsOffensive": 0,
                            "reboundsTotal": 1,
                            "steals": 0,
                            "threePointersAttempted": 2,
                            "threePointersMade": 0,
                            "threePointersPercentage": 0.0,
                            "turnovers": 0,
                            "twoPointersAttempted": 2,
                            "twoPointersMade": 1,
                            "twoPointersPercentage": 0.5,
                        },
                        "name": "James Ennis III",
                        "nameI": "J. Ennis III",
                        "firstName": "James",
                        "familyName": "Ennis III",
                    }
                ],
                "statistics": {
                    "assists": 14,
                    "assistsTurnoverRatio": 1.07692307692308,
                    "benchPoints": 33,
                    "biggestLead": 1,
                    "biggestLeadScore": "4-3",
                    "biggestScoringRun": 13,
                    "biggestScoringRunScore": "72-101",
                    "blocks": 1,
                    "blocksReceived": 4,
                    "fastBreakPointsAttempted": 7,
                    "fastBreakPointsMade": 2,
                    "fastBreakPointsPercentage": 0.28571428571428603,
                    "fieldGoalsAttempted": 94,
                    "fieldGoalsEffectiveAdjusted": 0.441489361702128,
                    "fieldGoalsMade": 38,
                    "fieldGoalsPercentage": 0.404255319148936,
                    "foulsOffensive": 2,
                    "foulsDrawn": 18,
                    "foulsPersonal": 16,
                    "foulsTeam": 14,
                    "foulsTechnical": 1,
                    "foulsTeamTechnical": 0,
                    "freeThrowsAttempted": 22,
                    "freeThrowsMade": 14,
                    "freeThrowsPercentage": 0.636363636363636,
                    "leadChanges": 4,
                    "minutes": "PT240M00.00S",
                    "minutesCalculated": "PT240M",
                    "points": 97,
                    "pointsAgainst": 124,
                    "pointsFastBreak": 8,
                    "pointsFromTurnovers": 10,
                    "pointsInThePaint": 52,
                    "pointsInThePaintAttempted": 47,
                    "pointsInThePaintMade": 26,
                    "pointsInThePaintPercentage": 0.553191489361702,
                    "pointsSecondChance": 20,
                    "reboundsDefensive": 31,
                    "reboundsOffensive": 15,
                    "reboundsPersonal": 46,
                    "reboundsTeam": 12,
                    "reboundsTeamDefensive": 4,
                    "reboundsTeamOffensive": 8,
                    "reboundsTotal": 58,
                    "secondChancePointsAttempted": 16,
                    "secondChancePointsMade": 9,
                    "secondChancePointsPercentage": 0.5625,
                    "steals": 5,
                    "threePointersAttempted": 28,
                    "threePointersMade": 7,
                    "threePointersPercentage": 0.25,
                    "timeLeading": "PT00M30.00S",
                    "timesTied": 0,
                    "trueShootingAttempts": 103.68,
                    "trueShootingPercentage": 0.46778549382716,
                    "turnovers": 11,
                    "turnoversTeam": 2,
                    "turnoversTotal": 13,
                    "twoPointersAttempted": 66,
                    "twoPointersMade": 31,
                    "twoPointersPercentage": 0.46969696969696995,
                },
            },
        },
    }

    arena = None
    away_team = None
    away_team_player_stats = None
    away_team_stats = None
    data_sets = None
    headers = None
    home_team = None
    home_team_player_stats = None
    home_team_stats = None
    game = None
    game_details = None
    nba_response = None
    officials = None

    def __init__(self, game_id, proxy=None, headers=None, timeout=30, get_request=True):
        self.game_id = game_id
        self.proxy = proxy
        if headers is not None:
            self.headers = headers
        self.timeout = timeout
        if get_request:
            self.get_request()

    def get_request(self):
        self.nba_response = NBALiveHTTP().send_api_request(
            endpoint=self.endpoint_url.format(game_id=self.game_id),
            parameters={},
            proxy=self.proxy,
            headers=self.headers,
            timeout=self.timeout,
        )
        self.load_response()

    def load_response(self):
        data_sets = self.nba_response.get_dict()
        if "game" in data_sets:
            self.game = Endpoint.DataSet(data=data_sets["game"])
            self.game_details = self.game.get_dict().copy()
            if "arena" in self.game.get_dict():
                self.arena = Endpoint.DataSet(data=data_sets["game"]["arena"])
                self.game_details.pop("arena")
            if "officials" in self.game.get_dict():
                self.officials = Endpoint.DataSet(data=data_sets["game"]["officials"])
                self.game_details.pop("officials")
            if "homeTeam" in self.game.get_dict():
                self.home_team = Endpoint.DataSet(data=data_sets["game"]["homeTeam"])

                # Home Team Player Stats
                self.home_team_player_stats = Endpoint.DataSet(
                    data=data_sets["game"]["homeTeam"]["players"]
                )

                # Home Team Stats
                home_team_stats = self.home_team.get_dict().copy()
                home_team_stats.pop("players")
                self.home_team_stats = Endpoint.DataSet(data=home_team_stats)

                self.game_details.pop("homeTeam")
            if "awayTeam" in self.game.get_dict():
                self.away_team = Endpoint.DataSet(data=data_sets["game"]["awayTeam"])

                # Away Team Player Stats
                self.away_team_player_stats = Endpoint.DataSet(
                    data=data_sets["game"]["awayTeam"]["players"]
                )

                # Away Team Stats
                away_team_stats = self.away_team.get_dict().copy()
                away_team_stats.pop("players")
                self.away_team_stats = Endpoint.DataSet(data=away_team_stats)

                self.game_details.pop("awayTeam")
            self.game_details = Endpoint.DataSet(data=self.game_details)


st.title("🏀 NBA Stats")
st.write(
    "Click in the download button to get the excel file with NBA players stats by team"
)

file_name = "nba_stats.xlsx"

# Número inicial
first_game_id = "0022400061"

# Extrai a parte inicial fixa e a parte numérica separadamente
prefix = first_game_id[:-3]  # "0022400"
number = int(first_game_id[-3:])  # 061, convertendo a última parte para um inteiro

# Quantidade de incrementos e criação da lista de IDs incrementados
num_ids = 10000  # Quantidade de IDs desejados
all_games_id = [f"{prefix}{number + i:03}" for i in range(num_ids)]


team_info = {}
desired_features = ["assists","blocks","fieldGoalsAttempted","fieldGoalsMade","points","reboundsTotal","steals","threePointersAttempted","threePointersMade","turnovers"]


# Caminho do arquivo onde a data da última execução será salva
date_file = 'last_run_date.txt'

# Função para salvar a data/hora atual no arquivo
def save_last_run_date():
    with open(date_file, 'w') as f:
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# Função para carregar a data/hora da última execução
def load_last_run_date():
    try:
        with open(date_file, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return "Nunca executado"
    
# Carregar a data/hora da última execução
last_run_date = load_last_run_date()
st.write(f"Data last execution: {last_run_date}")



# Botão para executar o código e salvar a data/hora atual
if st.button("Update Excel File"):
    # Aqui você coloca o código que deseja executar ao pressionar o botão
    st.write("Execute code can take several minutes...")

    

    for game_id in all_games_id:

        try: 
            home_team_name = BoxScore(game_id).get_dict()["game"]["homeTeam"]["teamName"]
            home_team_players = BoxScore(game_id).get_dict()["game"]["homeTeam"]["players"]

            home_players_stats = []
            home_players_name = []

            for home_player in home_team_players:

                player_stats = home_player["statistics"]
                player_stats_filtered = {chave: player_stats[chave] for chave in desired_features if chave in player_stats}

                player_name = home_player["name"]

                home_players_stats.append(player_stats_filtered)
                home_players_name.append(player_name)
                home_players_info = (home_players_name,home_players_stats)
            

            if home_team_name in team_info.keys():
                games_updated = team_info[home_team_name]
                games_updated.append(home_players_info)
                team_info[home_team_name] = games_updated
            else:
                team_info[home_team_name] = [home_players_info]
            # pd.DataFrame(home_players_stats,home_players_name)

            away_team_name = BoxScore(game_id).get_dict()["game"]["awayTeam"]["teamName"]
            away_team_players = BoxScore(game_id).get_dict()["game"]["awayTeam"]["players"]

            away_players_stats = []
            away_players_name = []

            for away_player in away_team_players:

                player_stats = away_player["statistics"]
                player_stats_filtered = {chave: player_stats[chave] for chave in desired_features if chave in player_stats}

                player_name = away_player["name"]

                away_players_stats.append(player_stats_filtered)
                away_players_name.append(player_name)
                away_players_info = (away_players_name,away_players_stats)
            

            if away_team_name in team_info.keys():
                games_updated = team_info[away_team_name]
                games_updated.append(away_players_info)
                team_info[away_team_name] = games_updated
            else:
                team_info[away_team_name] = [away_players_info]
            # pd.DataFrame(away_players_stats,away_players_name)
        except:
            print(f"O jogo com id {game_id} não foi encontrado")
            break
    with pd.ExcelWriter(file_name, engine='xlsxwriter') as writer:
        # Configura as cores para alternância
        cor1 = '#FFFF99'  # Amarelo claro
        cor2 = '#99CCFF'  # Azul claro

        for team in team_info.keys():
            # Combina os dados das partidas em um DataFrame único
            df_merged = pd.DataFrame()
            df1 = pd.DataFrame(team_info[team][0][1], index=team_info[team][0][0])
            
            for game in range(1, len(team_info[team])):
                df2 = pd.DataFrame(team_info[team][game][1], index=team_info[team][game][0])
                df_merged = pd.concat([df_merged, df2], axis=1) if game > 1 else pd.concat([df1, df2], axis=1)

            # Salva o DataFrame na aba correspondente, incluindo a coluna de índice
            df_merged.to_excel(writer, sheet_name=team, index=True)
            
            # Obtém o workbook e a aba (worksheet)
            workbook = writer.book
            worksheet = writer.sheets[team]

            # Aplica as cores alternadas em cada grupo de 10 colunas (incluindo a coluna de índice)
            for col_num in range(0, df_merged.shape[1] + 1):  # Inclui a coluna de índice
                # Define a cor com base no grupo de 10 colunas, ignorando a primeira coluna de índice
                fill_color = cor1 if (col_num - 1) // 10 % 2 == 0 else cor2
                col_letter = xl_col_to_name(col_num)  # Converte o número da coluna para a letra correspondente

                # Define o intervalo até a linha 19
                cell_range = f"{col_letter}2:{col_letter}20"  # Exclui o cabeçalho (linha 1) do intervalo

                # Aplica o formato no intervalo específico
                fmt = workbook.add_format({'bg_color': fill_color})
                worksheet.conditional_format(cell_range, {'type': 'no_blanks', 'format': fmt})

                # Ajusta a largura da coluna com base no maior conteúdo da coluna
                if col_num == 0:
                    # Para a coluna de índice
                    max_length = max([len(str(val)) for val in df_merged.index.astype(str)] + [len("Índice")])
                else:
                    # Para outras colunas
                    max_length = max(
                        [len(str(cell)) for cell in df_merged.iloc[:, col_num - 1].astype(str)]  # Maior comprimento do conteúdo
                        + [len(str(df_merged.columns[col_num - 1]))]  # Considera o cabeçalho
                    )

                worksheet.set_column(f"{col_letter}:{col_letter}", max_length + 2)  # Define a largura com uma margem

    # Salva a data e hora da última execução
    save_last_run_date()

    # Atualiza a data/hora da última execução na interface
    st.write(f"Data last update updated to: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    



with open(file_name, "rb") as f:
    excel_data = f.read()








st.download_button(
    label="Baixar Excel",
    data=excel_data,
    file_name= file_name,
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)
