<script>
	import { cn } from "$lib/components/shadcn/utils.js";

	let { ref = $bindable(null), class: className, children, ...restProps } = $props();
</script>

<div
	bind:this={ref}
	data-sidebar="header"
	class={cn("flex flex-col gap-2 p-2", className)}
	{...restProps}
>
	{@render children?.()}
</div>
