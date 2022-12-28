class Solution {
public:
    int minStoneSum(vector<int>& piles, int k) {
        priority_queue<int> heap(piles.begin(),piles.end());
        for (int i = 0; i < k; i++) {
            int largest_pile = heap.top();
            heap.pop();
            int new_pile = largest_pile / 2;
            heap.push(largest_pile - new_pile);
        }
        int total_stones = 0;
        while (!heap.empty()) {
            total_stones += heap.top();
            heap.pop();
        }
        return total_stones;
    }
};
