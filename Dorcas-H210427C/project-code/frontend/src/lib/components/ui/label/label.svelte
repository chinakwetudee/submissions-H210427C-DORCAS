<script>
	import { Label as LabelPrimitive } from "bits-ui";
	import { cn } from "$lib/components/shadcn/utils.js";

	let { ref = $bindable(null), class: className, ...restProps } = $props();
</script>

<LabelPrimitive.Root
	bind:ref
	class={cn(
		"text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70",
		className
	)}
	{...restProps}
/>
