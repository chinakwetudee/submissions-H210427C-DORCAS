<script>
	import { cn } from "$lib/components/shadcn/utils.js";

	let { ref = $bindable(null), class: className, children, ...restProps } = $props();
</script>

<p bind:this={ref} class={cn("text-muted-foreground text-sm", className)} {...restProps}>
	{@render children?.()}
</p>
