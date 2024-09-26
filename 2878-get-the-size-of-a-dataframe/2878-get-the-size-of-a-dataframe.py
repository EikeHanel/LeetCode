import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    ans_tup = players.shape
    ans = [ans_tup[0], ans_tup[1]]
    return ans