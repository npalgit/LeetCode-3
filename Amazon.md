### Amazon
* 146	LRU Cache
* 1		Two Sum
* 297	Serialize and Deserialize Binary Tree
* 460	LFU Cache
* 200	Number of Islands
* 438	Find All Anagrams in a String
* 236	Lowest Common Ancestor of a Binary Tree
* 138	Copy List with Random Pointer
* 20	Valid Parentheses
* 238	Product of Array Except Self
* 387	First Unique Character in a String
* 239	Sliding Window Maximum
* 17	Letter Combinations of a Phone Number
* 48	Rotate Image
* 121	Best Time to Buy and Sell Stock
* 5		Longest Palindromic Substring
* 240	Search a 2D Matrix II
* 206	Reverse Linked List
* 235	Lowest Common Ancestor of a Binary Search Tree
* 42	Trapping Rain Water
* 380	Insert Delete GetRandom O(1
* 127	Word Ladder
* 155	Min Stack
* 449	Serialize and Deserialize BST
* 141	Linked List Cycle
* 242	Valid Anagram
* 215	Kth Largest Element in an Array
* 160	Intersection of Two Linked Lists
* 2		Add Two Numbers
* 139	Word Break
* 49	Group Anagrams
* 126	Word Ladder II
* 234	Palindrome Linked List
* 98	Validate Binary Search Tree
* 167	Two Sum II - Input array is sorted
* 3		Longest Substring Without Repeating Characters
* 23	Merge k Sorted Lists
* 21	Merge Two Sorted Lists
* 15	3Sum
* 78	Subsets
* 102	Binary Tree Level Order Traversal
* 73	Set Matrix Zeroes
* 89	Gray Code
* 355	Design Twitter
* 204	Count Primes
* 414	Third Maximum Number
* 186	Reverse Words in a String II
* 8		String to Integer (atoi
* 199	Binary Tree Right Side View
* 119	Pascal's Triangle II
* 396	Rotate Function
* 451	Sort Characters By Frequency
* 459	Repeated Substring Pattern


#### OA2
* number of valid parentheses
```java
public class Solution {
    public int isValid(String s) {
        Stack<Character> stack = new Stack<>();
        for (char c : s.toCharArray()) {
            if (c == '(') {
                stack.push(')');
            } else if (stack.isEmpty() || stack.pop() != c) {
                return -1;
            }
        }
        return stack.isEmpty() ? s.length() / 2 : -1;
    }
}
```

* BST minimum sum path
```java
public class Solution {
    public int minDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        if (root.left != null && root.right == null) {
            return minDepth(root.left) + root.val;
        }
        if (root.left == null && root.right != null) {
            return minDepth(root.right) + root.val;
        }
        return Math.min(minDepth(root.left), minDepth(root.right)) + root.val;
    }
}
```

* Reverse Second Half of Linked List
```java
public class Solution {
    public ListNode reverseList(ListNode head) {
        if (head == null) {
            return null;
        }
        ListNode slow = head, fast = head;
        while (fast.next != null && fast.next.next != null) {
            fast = fast.next.next;
            slow = slow.next;
        }
        ListNode left = null, mid = slow.next, right = null;
        while (mid != null) {
            right = mid.next;
            mid.next = left;
            left = mid;
            mid = right;
        }
        slow.next = left;
        ListNode ptr = head;
        return head;
    }
}
```

* Rotate Matrix
```java
public class Rotate {
	void rotateMatrix(int mat[][]) {
    	// Consider all squares one by one
    	for (int i = 0; i < N / 2; i++) {
    	    // Consider elements in group of 4 in current square
    	    for (int j = i; j < N-i-1; j++) {
    	        // store current cell in temp variable
    	        int temp = mat[i][j];
 
    	        // move values from right to top
    	        mat[i][j] = mat[j][N-1-i];
 
    	        // move values from bottom to right
    	        mat[j][N-1-i] = mat[N-1-i][N-1-j];
 
    	        // move values from left to bottom
    	        mat[N-1-i][N-1-j] = mat[N-1-j][i];
 
    	        // assign temp to left
    	        mat[N-1-j][i] = temp;
    	    }
    	}
    }
}

public static int[][] rotate(int[][] matrix, int flag)
{
    if(matrix == null || matrix.length == 0) 
    	return matrix;
    int m = matrix.length, n = matrix[0].length;
    int[][] res = new int[n][m];
    for(int i = 0; i < m; i++)
        for(int j = 0; j < n; j++)
        	res[j][i] = matrix[i][j];

    if(flag == 1) {
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m / 2; j++) {
                int tmp = res[i][j];
                res[i][j] = res[i][m - 1 - j];
                res[i][m - 1 - j] = tmp;
            }
        }
    }
    else {
        for(int j = 0; j < m ;j++) {
            for(int i = 0; i < n / 2; i++) {
                int tmp = res[i][j];
                res[i][j] = res[n - 1 - i][j];
                res[n - 1 - i][j] = tmp;
            }
        }
    }
    return res;
}
```

* LongestPalidrome
```java
public class Solution {
    public int longestPalindrome(String s) {
        if (s == null || s.length() == 0)
            return 0;
        Set<Character> hs = new HashSet<>();
        int cnt = 0;
        for (char c : s.toCharArray()) {
            if (hs.contains(c)) {
                hs.remove(c);
                cnt += 1;
            } else {
                hs.add(c);
            }
        }
        return hs.isEmpty() ? cnt * 2 : cnt * 2 + 1;
    }
}
```

* RectangleOverlap
```java
// Returns true if two rectangles (l1, r1) and (l2, r2) overlap
bool doOverlap(Point l1, Point r1, Point l2, Point r2)
{
    // If one rectangle is on left side of other
    if (l1.x > r2.x || l2.x > r1.x)
        return false;
 
    // If one rectangle is above other
    if (l1.y < r2.y || l2.y < r1.y)
        return false;
 
    return true;
}
```

* deepCopy listNode
```java
public class Solution {
    public RandomListNode copyRandomList(RandomListNode head) {
        if (head == null)
            return null;
        Map<RandomListNode, RandomListNode> hm = new HashMap<>();
        RandomListNode node = head;
        while (node != null) {
            hm.put(node, new RandomListNode(node.label));
            node = node.next;
        }
        node = head;
        while (node != null) {
            hm.get(node).next = hm.get(node.next);
            hm.get(node).random = hm.get(node.random);
            node = node.next;
        }
        
        return hm.get(head);
    }
}
```

* K Closest Points
```java
class Point{
	int a;
	int b;
	public Point(int i, int j) {
		a = i;
		b = j;
	}
}

public Point[] findTopK(Point[] array, Point origin, int k) {
	Point[] res = new Point[k];
	PriorityQueue<Point> pq = new PriorityQueue<Point>(k, new Comparator<Point>(){
		public int compare(Point a, Point b) {
			return (int) getDistance(b, origin) - getDistance(a, origin);
		}
	});
		
	for(int i = 0; i < array.length(); i++) {
		if (i < k)
           	pq.offer(array[i]);
       	else {
        	Point temp = pq.peek();
           	if (getDistance(array[i], origin) < getDistance(temp, origin)) {
               pq.poll();
               pq.offer(array[i]);
        	}
    	}
    }
    	
   	while (!pq.isEmpty())
    	res[i] = pq.poll();
		
	return res;
}

public int getDistance(Point p1, Point p2) {
	return (int) Math.sqrt((p1.a - p2.a) * (p1.a - p2.a) + (p1.b - p2.b) * (p1.b - p2.b));
}
```

* Window Sum
```java
public List<Integer> GetSum(List<Integer> A, int k) {
	List<Integer> res  = new ArrayList<>();
   	if (A == null || A.size() == 0 || k <= 0)
   		return res;
   	int sum = 0;
   	for (int i = 0; i < k; i++) {
        sum += A.get(i);
    }
    res.push_back(sum);
    for (int i = 0; i < A.size() - k; i++) { //注意这里的个数, 前面以及把第一项加进去了!!  所以不是size - k + 1
        sum = sum - A.get(i) + A.get(i + k);
        res.push_back(sum);
    }
    return res;
}
```

* Maze
```java
public static boolean maze(int[][] m) {
	if(m == null || m.length == 0 || m[0][0] == 0) return false;
	int w = m[0].length, h = m.length;
	return dfs(m, 0, 0, w, h);
}

public static boolean dfs(int[][] m, int i, int j, int w, int h) {
	if(i > h - 1 || j > w - 1 || i < 0 || j < 0 || m[i][j] == 0 || m[i][j] == 2) 
		return false;
	if(m[i][j] == 9)
		return true;

	m[i][j] = 2;
	boolean left = dfs(m, i, j - 1, w, h);
	boolean right = dfs(m, i, j + 1, w, h);
	boolean up = dfs(m, i - 1, j, w, h);
	boolean down = dfs(m, i + 1, j, w, h);
	m[i][j] = 1;
	return left || right || up || down;
}
```

* Level Field OA Pilot
```python
def levelField(numRows, numColumns, field):
    # WRITE YOUR CODE HERE
    height_coord = []
    for i in range(numRows):
        for j in range(numColumns):
            if field[i][j] > 1:
                height_coord.append((field[i][j], (i, j)))
    ordered_height_coord = sorted(height_coord)
    
    res = 0
    for i, (height, coord) in enumerate(ordered_height_coord):
        if not i % 2:
            dest_coord = ordered_height_coord[i][1]
            cur_coord = ordered_height_coord[i-1][1] if i > 0 else (0, 0)
            
            if i + 1 < len(ordered_height_coord):
                next_height, next_coord = ordered_height_coord[i + 1]
            else:
                next_height, next_coord = -1, (-1, -1)
            
            q = [(dest_coord, 0)]
            step_map = {dest_coord: 0}
            
            while q:
                (x, y), step = q.pop(0)
                
                for dx, dy in (-1, 0), (0, 1), (1, 0), (0, -1):
                    nx, ny = x + dx, y + dy
                    if nx >= 0 and ny >= 0 and nx < numRows and ny < numColumns and \
                    (field[nx][ny] == 1 or field[nx][ny] == next_height) and \
                    (nx, ny) not in step_map:
                        q.append(((nx, ny), step + 1))
                        step_map[(nx, ny)] = step + 1
                
            if cur_coord not in step_map or next_coord != (-1, -1) and next_coord not in step_map:
                return -1
                
            dest_x, dest_y = dest_coord
            field[dest_x][dest_y] = 1
            
            if next_coord == (-1, -1):
                res += step_map[cur_coord]
            else:
                res += step_map[cur_coord] + step_map[next_coord]
            
                next_x, next_y = next_coord
                field[next_x][next_y] = 1
            
    return res
```
