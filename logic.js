var addTwoNumbers = function(l1, l2) {
	const control = (r1, r2, node, a) => {
        r1 = r1 == null || r1 == undefined ? new ListNode(0) : r1;
		r2 = r2 == null || r2 == undefined ? new ListNode(0) : r2;
		let b = r1.val + r2.val + a >= 10 ? 1 : 0;
		node.val = b == 1 ? r1.val  + r2.val - 10 + a : r1.val + r2.val + a;
		a = b == 1 ? 1 : 0;
		if(r1.next == null && r2.next == null && a == 0){
			return ;
		}
		node.next = new ListNode(0);
		control(r1.next, r2.next, node.next, a);
	}
	let node = new ListNode(0);
	control(l1, l2, node, 0);
	return node;
};
