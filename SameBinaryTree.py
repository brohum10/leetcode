{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red89\green138\blue67;\red24\green24\blue24;\red202\green202\blue202;
\red70\green137\blue204;\red67\green192\blue160;\red212\green214\blue154;\red183\green111\blue179;}
{\*\expandedcolortbl;;\cssrgb\c41569\c60000\c33333;\cssrgb\c12549\c12549\c12549;\cssrgb\c83137\c83137\c83137;
\cssrgb\c33725\c61176\c83922;\cssrgb\c30588\c78824\c69020;\cssrgb\c86275\c86275\c66667;\cssrgb\c77255\c52549\c75294;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs32 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 # Definition for a binary tree node.\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # class TreeNode:\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 #     def __init__(self, val=0, left=None, right=None):\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 #         self.val = val\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 #         self.left = left\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 #         self.right = right\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 class\cf4 \strokec4  \cf6 \strokec6 Solution\cf4 \strokec4 :\cb1 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     \cf5 \strokec5 def\cf4 \strokec4  \cf7 \strokec7 isSameTree\cf4 \strokec4 (self, p: \cf6 \strokec6 Optional\cf4 \strokec4 [TreeNode], q: \cf6 \strokec6 Optional\cf4 \strokec4 [TreeNode]) -> \cf6 \strokec6 bool\cf4 \strokec4 :\cb1 \
\cb3         \cf8 \strokec8 if\cf4 \strokec4  \cf8 \strokec8 not\cf4 \strokec4  p \cf8 \strokec8 and\cf4 \strokec4  \cf8 \strokec8 not\cf4 \strokec4  q:\cb1 \
\cb3             \cf8 \strokec8 return\cf4 \strokec4  \cf5 \strokec5 True\cf4 \cb1 \strokec4 \
\cb3         \cf8 \strokec8 if\cf4 \strokec4  p \cf8 \strokec8 and\cf4 \strokec4  q \cf8 \strokec8 and\cf4 \strokec4  p.val == q.val:\cb1 \
\cb3             \cf8 \strokec8 return\cf4 \strokec4  self.isSameTree(p.left, q.left) \cf8 \strokec8 and\cf4 \strokec4  self.isSameTree(p.right, q.right)\cb1 \
\cb3         \cf8 \strokec8 else\cf4 \strokec4 :\cb1 \
\cb3             \cf8 \strokec8 return\cf4 \strokec4  \cf5 \strokec5 False\cf4 \cb1 \strokec4 \
}