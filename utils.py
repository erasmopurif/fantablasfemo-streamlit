def cost2confirm(cost):
    cost = int(cost)
    if cost <= 7:
        return 0
    if cost > 7 and cost <= 15:
        return 5
    if cost > 15 and cost <= 20:
        return 10
    if cost > 20 and cost <= 25:
        return 15
    if cost > 25 and cost <= 30:
        return 20
    if cost > 30:
        return 25


# def get_team_dicts(teams_html):
#     teams = {}
#     for team in teams_html:
#         idx = int(team["data-id"])
#         teams[idx] = {}
#         teams[idx]["name"] = team.h4.text 
#         teams[idx]["trainer"] = team.h5.text
#         teams[idx]["res_coins"] = team.small.next.next.strip()
        
#         roster = team.table.tbody.find_all("tr")[:25]
#         roster_dict = {}
#         for p in roster:
#             pidx = int(p["data-id"])
#             roster_dict[pidx] = {}
#             roster_dict[pidx]["name"] = p.find("td", {"data-key": "name"}).text.title()
#             roster_dict[pidx]["club"] = p.find("td", {"data-key": "team"}).text.upper()
#             roster_dict[pidx]["price"] = int(p.find("td", {"data-key": "price"}).text)
#             roster_dict[pidx]["cost"] = int(p.find("td", {"data-key": "cost"}).text)
#             roster_dict[pidx]["confirm"] = cost2confirm(roster_dict[pidx]["cost"])
#         teams[idx]["roster"] = roster_dict
    
#     return teams

def get_team_dicts(teams_html):
    teams = {}
    for team in teams_html:
        team_name = team.h4.text 
        teams[team_name] = {}
        teams[team_name]["id"] = int(team["data-id"])
        teams[team_name]["trainer"] = team.h5.text
        teams[team_name]["res_coins"] = team.small.next.next.strip()
        
        roster = team.table.tbody.find_all("tr")[:25]
        roster_dict = {}
        for p in roster:
            p_name = p.find("td", {"data-key": "name"}).text.title()
            roster_dict[p_name] = {}
            roster_dict[p_name]["id"] = int(p["data-id"])
            roster_dict[p_name]["role"] = p.find("td", {"data-key": "role"}).text.upper()
            roster_dict[p_name]["club"] = p.find("td", {"data-key": "team"}).text.upper()
            roster_dict[p_name]["price"] = int(p.find("td", {"data-key": "price"}).text)
            roster_dict[p_name]["cost"] = int(p.find("td", {"data-key": "cost"}).text)
            roster_dict[p_name]["confirm"] = cost2confirm(roster_dict[p_name]["cost"])
        teams[team_name]["roster"] = roster_dict
    
    return teams
