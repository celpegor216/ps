# [Gold IV] Drop7 - 9389 

[문제 링크](https://www.acmicpc.net/problem/9389) 

### 성능 요약

메모리: 112136 KB, 시간: 180 ms

### 분류

구현, 시뮬레이션

### 제출 일자

2024년 10월 7일 20:10:32

### 문제 설명

<p><img alt="" src="https://www.acmicpc.net/upload/images2/drop71.png" style="float:right; height:281px; width:250px">Drop7 is a single-player game played on a 7 × 7 vertical grid. Initially, the grid is empty. In each turn, you will be given a disc on which a number between 1 and 7 is written and you have to drop it into one of the 7 columns from the above. It falls down the 7th row of the selected column, until it reaches above an already occupied cell or touches the ground in the first (bottom) row. For example, in Figure 1, dropping the disc into the first (leftmost) column causes it to stand in the second row (above 6) and dropping it into the third column causes it to hit the ground and to stay in the first row.</p>

<p>After dropping the given disc in a turn, each disc having a number equal to the size of its group-row or group-column will disappear (we will shortly define group-row and group-column). We know that all the discs that are subject to disappear will fade simultaneously. After that, all discs that the disc below them has been disappeared will fall down as far as possible. Then, the disappearance condition will be checked again on all the available discs again and if some disc number matches their group-row/column size, the loop continues. Otherwise, the next turn comes and a new disc will be dropped.</p>

<p><img alt="" src="https://www.acmicpc.net/upload/images2/drop72.png" style="float:right; height:269px; width:251px">The group-column of a disc is the number of discs that are already placed in the same column, including itself. For example, if we drop the disc 3 into the first column (as in Figure 1), its group-column will have the size of 2 and nothing happens. But, if we drop it into the 4th column from the left, the disc will disappear (because the group-column consists of three discs, 7, 7, and 3). Interestingly, if we drop this disc over the 7th (rightmost) column, not only the disc itself will disappear, but also the other 3 will disappear at the same time! More interestingly, if we drop this disc on the 2nd column, two discs will be removed in two steps – first the disc 4 will disappear as the column size (after putting 3 over it) will be 4. Then, after removal of 4, disc 3 will fall down over the two fives and then disappears by the same rule of matching number with group- column size.</p>

<p>Group-row size of a disc, however, is the number of discs connectedly in the same row of the disc. For example, in Figure 2, if we drop disc 1 into the second column, the group-row size of it, besides the 5 in the first column, would be two. But, if we drop it into the last column, the group-row size of both of 3’s will be come 3 and they both will disappear at the same time. Then, the disc 1 will have group-row size of 1 and will disappear by itself!</p>

<p>Starting with an empty board, you will be given some disc-drop actions. You just have to simulate the game and write down the final state of the board in the output.</p>

### 입력 

 <p>The input consists of several test cases. Each test case begins with a line containing the number n (1 ≤ n ≤ 1000) which is the number of discs dropped. In the following next n lines, n pairs of vi ci will be given, which states that at turn i, a dsic with number vi is dropped into the column ci. It is guaranteed that 1 ≤ vi, ci ≤ 7. The last line of the input contains a single zero.</p>

### 출력 

 <p>For each test case of the input, write seven lines of length seven, indicating the disc numbers in the grid. Put a hash sign (#) for empty cells. See the sample output for clarification. If during the game, a disc is dropped into a column that already contains 7 discs, just write “Game Over!” for the output of the test case. Write a blank link after the output of each test case.</p>

