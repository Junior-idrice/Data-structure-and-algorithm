import java.util.HashMap;
import java.util.Map;

public class TwoSum {
    public static int[] twoSum(int[] nums, int target){

            Map<Integer, Integer> map= new HashMap<>();

            for(int i=0; i<nums.length; i++){
                int complement = target - nums[i];

                if(map.containsKey(complement)){
                    return new int[] {map.get(complement),i};
                }
                map.put(nums[i], i );
            }
            // in case no solution found, but this not possible
           return new int[]{};

    }

    public static void  main(String[] args){

        int[] numbers = {4,1,2,5,8,9};
        int[] values = twoSum(numbers, 9);
        System.out.println(values[0]);
        System.out.println(values[1]);
    }
}
