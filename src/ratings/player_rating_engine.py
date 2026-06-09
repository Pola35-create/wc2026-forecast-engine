def compute_player_overall(player):
    return (
        player.attack_rating * 0.34 +
        player.midfield_rating * 0.33 +
        player.defense_rating * 0.33
    )