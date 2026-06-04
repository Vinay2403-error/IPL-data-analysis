import pandas as pd

df = pd.read_csv("IPL.csv", low_memory=False)

while True:
    print("\n===== IPL DATA ANALYSIS =====")
    print("1. Most Successful Team")
    print("2. Maximum runs")
    print("3. Maximum wickets")
    print("4. Most Sixes")
    print("5. Most Fours")
    print("6. Best Economy Bowler")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        team_runs = df.groupby('batting_team')['runs_total'].sum()
        print("\nMost Successful Team:")
        print(team_runs.sort_values(ascending=False).head(1))

    elif choice == 2:
        orange_cap = df.groupby('batter')['runs_batter'].sum()
        print("\nMaximum Runs:")
        print(orange_cap.sort_values(ascending=False).head(1))

    elif choice == 3:
        wickets = df[df['wicket_kind'].notna()]
        purple_cap = wickets.groupby('bowler').size()
        print("\nMaximum Wicket Taker:")
        print(purple_cap.sort_values(ascending=False).head(1))

    elif choice == 4:
        sixes = df[df['runs_batter'] == 6]
        most_sixes = sixes.groupby('batter').size()
        print("\nMost Sixes:")
        print(most_sixes.sort_values(ascending=False).head(1))

    elif choice == 5:
        fours = df[df['runs_batter'] == 4]
        most_fours = fours.groupby('batter').size()
        print("\nMost Fours:")
        print(most_fours.sort_values(ascending=False).head(1))

    elif choice == 6:
        bowler_runs = df.groupby('bowler')['runs_total'].sum()

        balls = df[df['valid_ball'] == True] \
                    .groupby('bowler').size()

        overs = balls / 6

        economy = bowler_runs / overs
        economy = economy[overs >= 50]

        print("\nBest Economy Bowler:")
        print(economy.sort_values().head(1))

    elif choice == 7:
        print("Thank You!")
        break

    else:
        print("Invalid Choice")