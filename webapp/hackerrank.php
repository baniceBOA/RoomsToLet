<?php
class Node{
    public $left,$right;
    public $data;
    function __construct($data)
    {
        $this->left=$this->right=null;
        $this->data = $data;
    }
}
class Solution{
    public function insert($root,$data){
        if($root==null){
            return new Node($data);
        }
        else{
            if($data<=$root->data){
                $cur=$this->insert($root->left,$data);
                $root->left=$cur;
            }
            else{
                $cur=$this->insert($root->right,$data);
                $root->right=$cur;
            }
            return $root;
        }
    }

	public function getHeight($root){
      //Write your code here
      $count_right = 0;
      $count_left = 0;
      if (isset($root)){
          if ($root->right){
            $count_right = 1+$this->getHeight($root->right);
          }
          if ($root->left){
            $count_left = 1+$this->getHeight($root->left);
          }
            
           
      }
      return ($count_right>$count_left)?$count_right:$count_left;
    }

}//End of Solution
$myTree=new Solution();
$root=null;
$T=intval(fgets());
while($T-->0){
    $data=intval(fgets());
    $root=$myTree->insert($root,$data);
}
$height=$myTree->getHeight($root);
echo $height;
?>
    