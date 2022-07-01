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


def get_team_dicts(teams_html):
    teams = {}
    for team in teams_html:
        team_name = team.h4.text 
        teams[team_name] = {}
        teams[team_name]["id"] = int(team["data-id"])
        teams[team_name]["trainer"] = team.h5.text
        teams[team_name]["res_coins"] = team.small.next.next.strip()
        
        roster = team.table.tbody.find_all("tr")[:-1]
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

        roster_dict_list = []
        for p in roster:
            p_dict = {}
            p_dict["role"] = p.find("td", {"data-key": "role"}).text.upper()
            p_dict["name"] = p.find("td", {"data-key": "name"}).text.title()
            p_dict["id"] = int(p["data-id"])
            p_dict["club"] = p.find("td", {"data-key": "team"}).text.upper()
            p_dict["price"] = int(p.find("td", {"data-key": "price"}).text)
            p_dict["cost"] = int(p.find("td", {"data-key": "cost"}).text)
            p_dict["confirm"] = cost2confirm(p_dict["cost"])
            roster_dict_list.append(p_dict)
        teams[team_name]["roster_table"] = roster_dict_list
    
    return teams


def compute_gain_confirm(roster, selected):
    total_gain = 0
    total_confirm = 0
    for p in roster:
        if p["name"] in selected:
            total_confirm += p["confirm"]
        else:
            total_gain += p["cost"]
    
    return total_gain, total_confirm
