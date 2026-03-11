## grub tricks

#### grubby aka grub2


#### check your kernel information

```bash
grubby --info=ALL
```

#### check your default kernel that is running

```bash
grubby --default-kernel
```

#### check your default index, 0

should be the latest kernel. If you are running a different index number
such as 1 or more then you are not on the latest kernel

```bash
grubby --default-index
```

#### set you index back to zero 0

```bash
gubby --set-default-index 0
```
