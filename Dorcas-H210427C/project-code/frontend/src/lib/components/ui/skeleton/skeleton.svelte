<script>
	import { cn } from "$lib/components/shadcn/utils.js";

	let { ref = $bindable(null), class: className, ...restProps } = $props();
</script>

<div
	bind:this={ref}
	class={cn("bg-primary/10 animate-pulse rounded-md", className)}
	{...restProps}
></div>
