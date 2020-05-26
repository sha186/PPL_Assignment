;;;Factorial without recursion

(defun fact_norm (n)
   (let ((f 1))
      (dotimes (i n) 
         (setf f (* f (+ i 1))))
      f
   )
)




;;;Factorial With Recursion

(defun fact_rec (N)
  "Compute the factorial of N."
  (if (= N 1)
      1
    (* N (fact_rec (- N 1)))))

;;;Finding nth element of list






(defun n_list(n lst)
       (let((count 1))
           (loop
               (cond((equal count n)(return (car lst))))
               (setq count (+ count 1))
               (setq lst (cdr lst)))))    
