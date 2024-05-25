def calculate_elo(player_a_rating, player_b_rating, outcome, k=32):
    """
    Calculate the new Elo rating for a player after a match.

    :param player_a_rating: Current rating of player A
    :param player_b_rating: Current rating of player B
    :param outcome: Outcome of the match from player A's perspective (1=win, 0=loss, 0.5=draw)
    :param k: K-factor (default is 32)
    :return: New rating for player A
    """
    expected_score_a = 1 / (1 + 10 ** ((player_b_rating - player_a_rating) / 400))
    new_rating_a = player_a_rating + k * (outcome - expected_score_a)
    return new_rating_a

if __name__ == "__main__":
    # Example usage
    player_a = 1600
    player_b = 1500
    outcome = 1  # Player A wins

    new_rating_a = calculate_elo(player_a, player_b, outcome)
    new_rating_b = calculate_elo(player_b, player_a, 1 - outcome)

    print(f"New rating for Player A: {new_rating_a}")
    print(f"New rating for Player B: {new_rating_b}")
