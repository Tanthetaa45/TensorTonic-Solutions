import ast
from typing import List
def baseline_predict(ratings_matrix: List[List[int]], target_pairs: List[List[int]]) -> List[float]:
    num_users: int = len(ratings_matrix)
    num_items: int = len(ratings_matrix[0])
    global_sum:int=0
    global_cnt:int=0
    user_sums:List[int]=[0]*num_users
    users_cnt:List[int]=[0]*num_users
    item_sum:List[int]=[0]*num_items
    item_cnt:List[int]=[0]*num_items
    for u in range(num_users):
        for i in range(num_items):
            rating:int=ratings_matrix[u][i]
            if rating!=0:
                global_sum+=rating
                global_cnt+=1
                user_sums[u]+=rating
                users_cnt[u]+=1
                item_sum[i]+=rating
                item_cnt[i]+=1
    global_mean:float=global_sum/global_cnt
    user_bias:List[float]=[0.0]*num_users
    for u in range(num_users):
        if users_cnt[u]>0:
            user_bias[u]=(user_sums[u]/users_cnt[u])-global_mean
    item_bias:List[float]=[0.0]*num_items
    for i in range(num_items):
        if item_cnt[i]>0:
            item_bias[i]=(item_sum[i]/item_cnt[i])-global_mean
    predictions:List[float]=[]
    for u,i in target_pairs:
        predicted_rating:float=global_mean+user_bias[u]+item_bias[i]
        predictions.append(predicted_rating)
    return predictions
# if __name__ == "__main__":
#     print("--- Collaborative Filtering Baseline Predictor ---")
#     print("Enter your inputs exactly as Python 2D lists.")
#     try:
#         matrix_input=input("Enter ratings_matrix (e.g., [[5, 3, 0], [4, 0, 1], [0, 1, 5]]): ")
#         ratings_matrix:List[List[int]]=ast.literal_eval(matrix_input)
#         pairs_input=input("Enter target_pairs (e.g., [[0, 2], [1, 1], [2, 0]]): ")
#         target_pairs:List[List[int]]=ast.literal_eval(pairs_input)
#         predictions=baseline_predict(ratings_matrix, target_pairs)
#         print("\nResults:")
#         print(f"Predictions: {predictions}")
#     except SyntaxError:
#         print("\nError: Invalid input format. Please ensure you are pasting valid nested lists with brackets and commas.")
#     except Exception as e:
#         print(f"\nAn unexpected error occurred: {e}")

