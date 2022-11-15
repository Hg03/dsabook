import streamlit as st
from pathlib import Path
from streamlit_option_menu import option_menu

st.set_page_config(page_title='DSABook',layout="wide")
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

array_problems = {"Select The Problems":None,"Two Sum":"array/Two_Sum.md","Best time to buy and sell stock":"array/Bttbass.md","Majority Element":"array/Majority_Element.md","Contains Duplicate":"array/Contain_Duplicate.md","Insert Interval":"array/Insert_Interval.md","3sum":"array/3sum.md","Product of Array Except Self":"array/Poaex.md","Combination Sum":"array/Combination_Sum.md","Merge Intervals":"array/Merge_Intervals.md","Sort Colors":"array/Sort_Colors.md","Container With Most Water":"array/Cwmw.md"}
linkedlist_problems = {"Select The Problems":None,"Merge Two Linked Lists":"linked_list/Merge2.md","Detect Cycle in linked list":"linked_list/LLcycle.md","Reverse Linked List":"linked_list/Reverse_List.md","Middle of the Linked List":"linked_list/Middle_Linked_List.md","LRU Cache":"linked_list/LRU_Cache.md"}
stack_problems = {"Select The Problems":None,"Valid Parentheses":"stack/Valid_Parentheses.md","Implement Queue Using Stacks":"stack/Q_using_Stack.md","Evaluate Reverse Polish Notation":"stack/RPN.md","Min Stack":"stack/Min_Stack.md","Trapping Rain Water":"stack/TRW.md","Basic Calculator":"stack/Basic_Calculator.md","Largest Rectangle in Histogram":"stack/Largest_Rectangle_in_Histogram.md"}
string_problems = {"Select The Problems":None,"Valid Palindrome":"string/Valid_Palindrome.md","Valid Anagram":"string/Valid_Anagram.md","Longest Palindrome":"string/Longest_Palindrome.md","Longest Substring Without Repeating Characters":"string/LSWRC.md","String to Integer":"string/Str_2_Int.md","Longest Palindromic Substring":"string/Longest_Palindromic_Substring.md","Minimum Window Substring":"string/Minimum_Window_Substring.md"}
binary_problems = {"Select The Problems":None,"Add Binary":"binary/Add_Binary.md"}
binary_tree_problems = {"Select The Problems":None,"Invert Binary Tree":"binary_tree/Invert_Bt.md","Balanced Binary Tree":"binary_tree/Balanced_Bt.md","Diameter of Binary Tree":"binary_tree/Diameter_Bt.md","Maximum Depth of Binary Tree":"binary_tree/Depth_of_Binary_Tree.md","Binary Tree Level Order Traversal":"binary_tree/Level_Order_Traversal.md","Lowest Common Ancestor of a Binary Tree":"binary_tree/LCABT.md","Binary Tree Right Side View":"binary_tree/Right_Side_View.md","Construct Binary Tree from Preorder and Inorder Traversal":"binary_tree/CBTPI.md","Serialize and Deserialize Binary Tree":"binary_tree/SD_Bt.md"}
binary_search_problems = {"Select The Problems":None,"Binary Search":"binary_search/Binary_Search.md","First Bad Version":"binary_search/First_Bad_Version.md","Search in Rotated Sorted Array":"binary_search/Search_in_RSa.md","Time Based Key-Value Store":"binary_search/TB_KeyValue_Store.md","Maximum Profit in Job Scheduling":"binary_search/MP_JS.md"}
binary_search_tree_problems = {"Select The Problems":None,"Lowest Common Ancestor of a Binary Search Tree":"binary_search_tree/LCABST.md","Validate Binary Search Tree":"binary_search_tree/Validate_BST.md","Kth Smallest Element in a Binary Search Tree":"binary_search_tree/K_Smallest_Element_BST.md"}
dp_problems = {"Select The Problems":None,"Climbing Stairs":"dynamicprogramming/Climbing_Stairs.md","Maximum Subarray":"dynamicprogramming/Maximum_Subarray.md","Coin Change":"dynamicprogramming/Coin_Change.md","Partition Equal Subset Sum":"dynamicprogramming/Partition_Equal_Subset_Sum.md","Unique Paths":"dynamicprogramming/Unique_Paths.md"}
hashtable_problems = {"Select The Problems":None,"Ransom Note":"hashtable/Ransom_Note.md"}
matrix_problems = {"Select The Problems":None,"Spiral Matrix":"matrix/SpiralMatrix.md"}
heap_problems = {"Select The Problems":None,"K Closest Points to Origin":"heap/KCP2O.md","Task Scheduler":"heap/TaskScheduler.md","Find Median From Data Stream":"heap/Median_From_Data_Stream.md","Merge K Sorted Lists":"heap/Merge_K_Sorted_Lists.md"}
graph_problems = {"Select The Problems":None,"Flood Fill":"graph/Flood_Fill.md","01 Matrix":"graph/01_Matrix.md","Clone Graph":"graph/Clone_Graph.md","Course Schedule":"graph/Course_Schedule.md","Number of Islands":"graph/Number_of_Islands.md","Rotting Oranges":"graph/Rotting_Oranges.md","Accounts Merge":"graph/Accounts_Merge.md","Word Search":"graph/Word_Search.md","Minimum Height Trees":"graph/Minimum_Height_Trees.md","Word Ladder":"graph/Word_Ladder.md"}
recursion_problems = {"Select The Problems":None,"Permutations":"recursion/Permutations.md","Subsets":"recursion/Subsets.md","Letter Combinations of a Phone Number":"recursion/LCOAPN.md"}
trie_problems = {"Select The Problems":None,"Implement TRIE":"trie/Implement_Trie.md","Word Break":"trie/Word_Break.md"}

options = {'Array':array_problems,"Linked List":linkedlist_problems,"Stack":stack_problems,"String":string_problems,"Binary":binary_problems,"Binary Tree":binary_tree_problems,"Binary Search Tree":binary_search_tree_problems,"Dynamic Programming":dp_problems,"Graph":graph_problems,"Matrix":matrix_problems,"Recursion":recursion_problems,"Hash Table":hashtable_problems,"Heap":heap_problems,"Trie":trie_problems}

st.sidebar.title("📖 DSA book")
st.markdown("# DSA Book")

# array_bar = st.sidebar.selectbox("Array",array_problems)
# linked_list_bar = st.sidebar.selectbox("Linked List",linkedlist_problems)
# stack_bar = st.sidebar.selectbox("Stack",stack_problems)
# string_bar = st.sidebar.selectbox("String",string_problems)
# binary_tree_problems = st.sidebar.selectbox("Binary Tree",binary_tree_problems)
# binary_search_bar = st.sidebar.selectbox("Binary Search",binary_search_problems)
# graph_bar = st.sidebar.selectbox("Graph",graph_problems)
# binary_search_tree_bar = st.sidebar.selectbox("Binary Search Tree",binary_search_tree_problems)
# hashtable_bar = st.sidebar.selectbox("Hashtable",hashtable_problems)
# dp_bar = st.sidebar.selectbox("DP",dp_problems)
# binary_bar = st.sidebar.selectbox("Binary",binary_problems)
# heap_bar = st.sidebar.selectbox("Heap",heap_problems)
# trie_bar = st.sidebar.selectbox("Trie",trie_problems)
# recursion_bar = st.sidebar.selectbox("Recursion",recursion_problems)
# matrix_bar = st.sidebar.selectbox("Matrix",matrix_problems)


with st.sidebar:
    nav_bar = option_menu(
        "Topics",
        list(options.keys()),
        menu_icon="code-slash",
        icons=['braces','link','archive','type-strikethrough','file-binary','bezier','tree-fill','border','graph-down','box','infinity','table','diagram-3','node-plus']
    )


problems = st.selectbox('List Of Problems',options[nav_bar].keys())

if(problems != 'Select The Problems' and problems in list(array_problems.keys())[1:]):
    st.markdown(Path(array_problems[problems]).read_text())

if(problems != 'Select The Problems' and problems in list(linkedlist_problems.keys())[1:]):
    st.markdown(Path(linkedlist_problems[problems]).read_text())

if(problems != 'Select The Problems' and problems in list(stack_problems.keys())[1:]):
    st.markdown(Path(stack_problems[problems]).read_text())

if(problems != 'Select The Problems' and problems in list(string_problems.keys())[1:]):
    st.markdown(Path(string_problems[problems]).read_text())

if(problems != 'Select The Problems' and problems in list(binary_problems.keys())[1:]):
    st.markdown(Path(binary_problems[problems]).read_text())

if(problems != 'Select The Problems' and problems in list(binary_tree_problems.keys())[1:]):
    st.markdown(Path(binary_tree_problems[problems]).read_text())

if(problems != 'Select The Problems' and problems in list(binary_search_problems.keys())[1:]):
    st.markdown(Path(binary_search_problems[problems]).read_text())

if(problems != 'Select The Problems' and problems in list(binary_search_tree_problems.keys())[1:]):
    st.markdown(Path(binary_search_tree_problems[problems]).read_text())

if(problems != 'Select The Problems' and problems in list(matrix_problems.keys())[1:]):
    st.markdown(Path(matrix_problems[problems]).read_text())

if(problems != 'Select The Problems' and problems in list(recursion_problems.keys())[1:]):
    st.markdown(Path(recursion_problems[problems]).read_text())

if(problems != 'Select The Problems' and problems in list(dp_problems.keys())[1:]):
    st.markdown(Path(dp_problems[problems]).read_text())

if(problems != 'Select The Problems' and problems in list(hashtable_problems.keys())[1:]):
    st.markdown(Path(hashtable_problems[problems]).read_text())

if(problems != 'Select The Problems' and problems in list(graph_problems.keys())[1:]):
    st.markdown(Path(graph_problems[problems]).read_text())

if(problems != 'Select The Problems' and problems in list(trie_problems.keys())[1:]):
    st.markdown(Path(trie_problems[problems]).read_text())

if(problems != 'Select The Problems' and problems in list(heap_problems.keys())[1:]):
    st.markdown(Path(heap_problems[problems]).read_text())

elif(problems == 'Select The Problems'):
    st.markdown(Path("index.md").read_text())




