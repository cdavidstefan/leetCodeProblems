// 125. Valid Palindrome Solution

let string = "civic";

function palindrome(s) {
  // Sanitize the string and lowercase
  s.toLowerCase().replace(/[\W_]/g, "");
  let left = 0;
  let right = s.length - 1;
  while (left < right) {
    if (s[left] !== s[right]) {
      return false;
    };
    left++;
    right--;
  };
  return true;
};
palindrome(string);

// 