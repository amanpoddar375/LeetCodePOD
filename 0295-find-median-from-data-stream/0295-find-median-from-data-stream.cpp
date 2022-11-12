class MedianFinder {
public:
    priority_queue<int>maxheap;
    priority_queue<int,vector<int>,greater<int>>minheap;
    MedianFinder() {
        
    }
    
    void addNum(int num) {
     if(maxheap.size()>0 && num>maxheap.top())
        {
            minheap.push(num);
        }
        else{
            maxheap.push(num);
        }
        if(maxheap.size()>minheap.size()+1)
        {
            minheap.push(maxheap.top());
            maxheap.pop();
        }
        if(minheap.size()>maxheap.size()+1)
        {
            maxheap.push(minheap.top());
            minheap.pop();
        }   
        
    }
    
    double findMedian() {
      if(maxheap.size()==minheap.size())
        {
            return (maxheap.top() + minheap.top())/2.0;
        }
                if(maxheap.size() > minheap.size())
                {
                    return maxheap.top();
                }
        else
        {
            return minheap.top();
        } 
    }
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */