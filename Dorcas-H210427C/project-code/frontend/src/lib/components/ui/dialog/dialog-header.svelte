<script>
	import { cn } from "$lib/components/shadcn/utils.js";
	let className = undefined;
	export { className as class };
</script>

<div class={cn("flex flex-col space-y-1.5 text-center sm:text-left", className)} {...$$restProps}>
	<slot />
</div>
